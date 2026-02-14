import pandas as pd
import unicodedata

path = "data/landing/activity_21851453697.csv"

df = pd.read_csv(path)

def normalize_columns(col):
    col = col.lower().strip()
    col = unicodedata.normalize('NFKC', col).encode("ascii", "ignore").decode("utf-8") # estudar isso aqui
    col = col.replace(" ", "_").replace(":", "")

    return col

df_col_normalized = df.copy()
df_col_normalized.columns = [normalize_columns(col) for col in df.columns]
print(df_col_normalized)