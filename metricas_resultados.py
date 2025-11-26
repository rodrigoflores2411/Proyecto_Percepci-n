import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

TRAIN_TEST_FILE = "metricas_train_test.csv"
CV_FILE = "metricas_cross_validation.csv"

def cargar_metricas():
    df_train = pd.read_csv(TRAIN_TEST_FILE)
    df_cv = pd.read_csv(CV_FILE)
    return df_train, df_cv

def generar_graficos(df_train, df_cv):
    import matplotlib.pyplot as plt

    print("Generando gráficos...")

    # -------------------------
    # GRÁFICO 1: COMPARACIÓN ACCURACY
    # -------------------------
    acc_train = df_train["accuracy"].mean()
    acc_cv = df_cv["accuracy"].mean()

    plt.figure()
    plt.bar(["Train/Test", "Cross-Validation"], [acc_train, acc_cv])
    plt.title("Comparación de Accuracy")
    plt.ylabel("Accuracy")
    plt.savefig("accuracy_comparacion.png")
    print("[OK] accuracy_comparacion.png generado")

    # -------------------------
    # GRÁFICO 2: CURVA LOSS / LATENCIA
    # -------------------------
    plt.figure()
    plt.plot(df_train["latencia"], marker='o')
    plt.title("Curva de Latencia por Fold (Train/Test)")
    plt.ylabel("Latencia (ms)")
    plt.xlabel("Fold")
    plt.savefig("curva_loss_accuracy.png")
    print("[OK] curva_loss_accuracy.png generado")

    # -------------------------
    # GRÁFICO 3: FPS por Fold
    # -------------------------
    plt.figure()
    plt.bar(df_train["fold"], df_train["fps"])
    plt.title("FPS por Fold (Train/Test)")
    plt.xlabel("Fold")
    plt.ylabel("FPS")
    plt.savefig("fps_folds.png")
    print("[OK] fps_folds.png generado")

    # -------------------------
    # GRÁFICO 4: Latencia por Fold
    # -------------------------
    plt.figure()
    plt.plot(df_train["fold"], df_train["latencia"], marker='o')
    plt.title("Latencia por Fold (Train/Test)")
    plt.xlabel("Fold")
    plt.ylabel("Latencia (ms)")
    plt.savefig("latencia_folds.png")
    print("[OK] latencia_folds.png generado")

    print("Todos los gráficos han sido generados.")
def main():
    print("Cargando métricas...")
    df_train, df_cv = cargar_metricas()

    print(df_train)
    print(df_cv)

    print("\nGenerando gráficos...")
    generar_graficos(df_train, df_cv)

    print("Gráficos generados:")
    print(" - grafico_accuracy_comparacion.png")
    print(" - grafico_latencia_folds.png")
    print(" - grafico_fps_folds.png")
    print(" - grafico_curva_loss_accuracy.png")
    print("\nListo.")

if __name__ == "__main__":
    main()
