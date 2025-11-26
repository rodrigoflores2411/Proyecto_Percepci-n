from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from pathlib import Path


spark = SparkSession.builder \
    .appName("KafkaStreamingConsumer_FacialRecognition") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Definir esquema de los eventos Kafka
schema = StructType([
    StructField("timestamp", StringType(), True),
    StructField("persona", StringType(), True),
    StructField("resultado", StringType(), True),
    StructField("confianza", FloatType(), True),
    StructField("latencia_ms", FloatType(), True),
    StructField("fps", FloatType(), True),
    StructField("audio_path", StringType(), True),
    StructField("record_hash", StringType(), True)
])

# Leer el stream desde Kafka
kafka_topic = "accesos_reconocimiento"

df_raw = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", kafka_topic) \
    .option("startingOffsets", "latest") \
    .load()

# Convertir mensajes a JSON estructurado

df_parsed = df_raw.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Mostrar en consola 
query_console = df_parsed.writeStream \
    .format("console") \
    .outputMode("append") \
    .option("truncate", False) \
    .start()

# Guardar en formato Parquet
warehouse_stream_path = str(Path("warehouse/stream").resolve())

query_parquet = df_parsed.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("path", warehouse_stream_path) \
    .option("checkpointLocation", warehouse_stream_path + "/checkpoint") \
    .start()


query_console.awaitTermination()
query_parquet.awaitTermination()
