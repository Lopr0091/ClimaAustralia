import pandas as pd

def explorar_datos(datos: pd.DataFrame) -> None:
    print("Primeras filas del dataset:")
    print(datos.head())

    print("\nResumen estadístico:")
    print(datos.describe(include="all"))

    print("\nValores nulos por columna:")
    print(datos.isnull().sum())

    print("\nDetección de valores atípicos (usando IQR):")
    for col in datos.select_dtypes(include=["float64", "int64"]).columns:
        q1 = datos[col].quantile(0.25)
        q3 = datos[col].quantile(0.75)
        iqr = q3 - q1
        outliers = ((datos[col] < (q1 - 1.5 * iqr)) | (datos[col] > (q3 + 1.5 * iqr))).sum()
        print(f"{col}: {outliers} posibles outliers")

    columnas_numericas = datos.select_dtypes(include=["float64", "int64"]).columns.tolist()

    if "Rainfall" in datos.columns:
        print("\nCorrelación con 'Rainfall':")
        print(datos[columnas_numericas].corrwith(datos["Rainfall"]))

    if "RainTomorrow" in datos.columns:
        print("\nCorrelación con 'RainTomorrow':")
        rain_tomorrow_num = datos["RainTomorrow"].map({"Yes": 1, "No": 0})
        datos_numericos = datos[columnas_numericas].copy()
        datos_numericos = datos_numericos.assign(RainTomorrow=rain_tomorrow_num)

        correlaciones = datos_numericos.corr()["RainTomorrow"].drop("RainTomorrow")
        print(correlaciones.sort_values(ascending=False))
