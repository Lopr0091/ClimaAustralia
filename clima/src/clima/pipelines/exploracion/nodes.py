import pandas as pd

def explorar_datos(datos: pd.DataFrame) -> None:
    print("Primeras filas del dataset:")
    print(datos.head())
    print("\nResumen estadístico:")
    print(datos.describe(include="all"))
    print("\nValores nulos por columna:")
    print(datos.isnull().sum())
