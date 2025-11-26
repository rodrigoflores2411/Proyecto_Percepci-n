# 🧠 Sistema de Reconocimiento Facial  
### Pipeline Batch + Streaming + Kafka + Spark + LBPH

---

## 1. Descripción del Proyecto
Este proyecto implementa un sistema completo de reconocimiento facial en tiempo real usando:

- **OpenCV LBPH** para reconocimiento facial  
- **Spark (Batch)** para procesar el dataset y generar el warehouse  
- **Kafka (Streaming)** para enviar eventos en tiempo real  
- **Spark Streaming** como consumidor distribuido  
- **Logging con Hash-Chain** para trazabilidad  
- **Métricas automáticas + visualizaciones**

El sistema funciona bajo una arquitectura híbrida **Batch + Streaming** que simula entornos de producción.

---

## 2. Instalación del Entorno Virtual

### Crear entorno virtual
```bash```
python -m venv .venv
Activar entorno
Windows PowerShell

```bash```
Copiar código
.\.venv\Scripts\Activate.ps1
Windows CMD

```bash```
Copiar código
.\.venv\Scripts\activate.bat
Linux/macOS

```bash```
Copiar código
source .venv/bin/activate
3. Instalación de Dependencias
bash
Copiar código
pip install -r requirements.txt
4. Estructura del Proyecto
pgsql
Copiar código
Proyecto_Percep/
│
├── dataset/
├── warehouse/
├── logs/
├── models/
│   ├── lbph_model.xml
│   └── labels.json
│
├── src/
│   ├── config.py
│   ├── metricas.py
│   ├── spark_ingest.py
│   ├── train_lbph.py
│   ├── recognize_realtime.py
│   └── spark_streaming_consumer.py
│
├── metricas_resultados.py
├── requirements.txt
└── README.md
5. Ejecución del Pipeline
5.1 Procesamiento Batch (Spark)
bash
Copiar código
python src/spark_ingest.py
Genera:

bash
Copiar código
warehouse/faces.parquet
5.2 Entrenamiento del Modelo LBPH
bash
Copiar código
python src/train_lbph.py
Genera:

bash
Copiar código
models/lbph_model.xml
models/labels.json
5.3 Métricas y Gráficos
bash
Copiar código
python metricas_resultados.py
Genera:

Copiar código
metricas_train_test.csv
metricas_cross_validation.csv
plots/
  accuracy_comparacion.png
  curva_loss_accuracy.png
  fps_folds.png
  latencia_folds.png
6. Ejecución del Sistema en Tiempo Real
6.1 Iniciar Apache Kafka
ZooKeeper

bash
Copiar código
zookeeper-server-start.bat config/zookeeper.properties
Kafka Server

bash
Copiar código
kafka-server-start.bat config/server.properties
Crear tópico

bash
Copiar código
kafka-topics.bat --create --topic accesos_reconocimiento --bootstrap-server localhost:9092
6.2 Reconocimiento Facial en Vivo
bash
Copiar código
python src/recognize_realtime.py
Ejemplo de mensaje enviado a Kafka:

json
Copiar código
{
  "timestamp": "2025-11-26 02:43:12",
  "persona": "Rodrigo",
  "resultado": "ACCESO_CONCEDIDO",
  "confianza": 42.1,
  "latencia_ms": 18.4,
  "fps": 58.2
}
6.3 Consumidor con Spark Streaming
bash
Copiar código
python src/spark_streaming_consumer.py
7. Notas Importantes
La carpeta .venv/ NO debe subirse al repositorio.

El archivo lbph_model.xml es grande y debe generarse localmente.

Si no existe warehouse/faces.parquet, debes ejecutar Spark ingest antes del entrenamiento.
