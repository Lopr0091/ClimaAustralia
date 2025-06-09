import os
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.SettingWithCopyWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)

def preparar_dataset(df: pd.DataFrame) -> pd.DataFrame:
    print("Preparando datos...")
    df_copia = df.copy()
    num_filas = df_copia.shape[0]
    print("\n--- Detección y eliminación de outliers ---")
    columnas_numericas = df_copia.select_dtypes(include=["float64", "int64"]).columns
    for col in columnas_numericas:
        if col == "Rainfall":
            continue
        q1 = df_copia[col].quantile(0.25)
        q3 = df_copia[col].quantile(0.75)
        iqr = q3 - q1
        lim_inf = q1 - 1.5 * iqr
        lim_sup = q3 + 1.5 * iqr
        df_copia = df_copia[(df_copia[col] >= lim_inf) & (df_copia[col] <= lim_sup)]
    print(f"Filas después de remover outliers: {df_copia.shape[0]} (de {num_filas})")
    print("\n--- Valores nulos ---")
    nulos_abs = df_copia.isnull().sum()
    nulos_pct = (nulos_abs / df_copia.shape[0] * 100).round(2)
    print(nulos_abs[nulos_abs > 0])
    print("\n--- Eliminando filas con nulos en columnas <9% ---")
    columnas_menos_9 = nulos_pct[nulos_pct < 9].index.tolist()
    df_copia = df_copia.dropna(subset=columnas_menos_9)
    print(f"Filas restantes: {df_copia.shape[0]}")
    print("\n--- Rellenando columnas con >=9% de nulos ---")
    columnas_mas_9 = nulos_pct[nulos_pct >= 9].index.tolist()
    for col in columnas_mas_9:
        if col in df_copia.columns:
            if df_copia[col].dtype in ['float64', 'int64']:
                mediana = df_copia[col].median()
                print(f"'{col}' rellena con mediana: {mediana}")
                df_copia[col] = df_copia[col].fillna(mediana)
            else:
                moda = df_copia[col].mode().iloc[0]
                print(f"'{col}' rellena con moda: {moda}")
                df_copia[col] = df_copia[col].fillna(moda)
    print("\n--- Dataset preparado ---")
    return df_copia