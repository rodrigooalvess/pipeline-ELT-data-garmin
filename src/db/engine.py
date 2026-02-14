from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def get_engine():


    try:
        load_dotenv()

        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_NAME = os.getenv("DB_NAME")

        url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        db = create_engine(url)

        with db.connect() as conn:
            print("Banco de Dados Conectado com Sucesso!")
        
        return db
    
    except Exception as erro:
        print(f"Erro ao Conectar ao Banco de Dados: {erro}")
    