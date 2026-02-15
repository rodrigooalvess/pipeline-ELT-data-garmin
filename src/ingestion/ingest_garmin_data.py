import pandas as pd
import unicodedata
import shutil
import os
from datetime import datetime
from src.db.engine import get_engine


def data_ingestion():
    raw_path = "data/landing/"
    processed_path = "data/processed/"

    files = [files for files in os.listdir(raw_path) if files.endswith(".csv")]

    if files:

        for file_name in files:

            file_name_path = f"{raw_path}{file_name}"
            file_name_path_processed = f"{processed_path}{file_name}"

            try:

                df = pd.read_csv(file_name_path)

                def normalize_columns(col):
                    col = col.lower().strip()
                    col = unicodedata.normalize("NFD", col).encode("ascii", "ignore").decode("utf-8")
                    col = col.replace(" ", "_").replace(":", "")

                    return col

                df_col_normalized = df.copy()
                df_col_normalized.columns = [normalize_columns(col) for col in df.columns]
                df_col_normalized.dropna(axis=1, how="all", inplace=True)

                df_col_normalized["file_source"] = file_name
                df_col_normalized["ingested_at"] = datetime.now()

                df_col_normalized.drop(df_col_normalized[df_col_normalized["intervalo"] == "Resumo"].index, inplace=True)

                engine = get_engine()

                df_col_normalized.to_sql(name="garmin_activities", con=engine, schema="raw", if_exists="append", index=False)

                shutil.move(file_name_path, processed_path)
                print(f"Arquivo: {file_name_path} processado e movido para {file_name_path_processed}")

                return True

            except Exception as erro:

                print(f"Erro ao processar {file_name}: {erro}")
    else:
        print("Nenhum Arquivo Novo Para Processar!")
        return  
