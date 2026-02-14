import pandas as pd
import unicodedata
import shutil
import os

raw_path = "data/landing/"
processed_path = "data/processed/"

files = [files for files in os.listdir(raw_path) if files.endswith(".csv")]

if files:

    for file_name in files:

        file_name_path = f"{raw_path}{file_name}"
        file_name_path_processed = f"{processed_path}{file_name}"

        df = pd.read_csv(file_name_path)

        def normalize_columns(col):
            col = col.lower().strip()
            col = unicodedata.normalize('NFKC', col).encode("ascii", "ignore").decode("utf-8")
            col = col.replace(" ", "_").replace(":", "")

            return col

        df_col_normalized = df.copy()
        df_col_normalized.columns = [normalize_columns(col) for col in df.columns]
        df_col_normalized.dropna(axis=1, how="all", inplace=True)

        print(df_col_normalized)

        #logica de mandar pro banco

        shutil.move(file_name_path, processed_path)
        print(f"Arquivo: {file_name_path} processado e movido para {file_name_path_processed}")
