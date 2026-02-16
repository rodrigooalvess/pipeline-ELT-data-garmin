from prefect import flow, task
import subprocess
from src.ingestion.ingest_garmin_data import data_ingestion

@task(name="Ingestion Garmin DATA", retries=2, retry_delay_seconds=30)
def run_ingestion():
    print("Iniciando Ingestão de Arquivos...")
    result =  data_ingestion() 
    return result

@task(name="Transformações do DBT")
def run_dtb():
    print("Iniciando DBT Run...")
    result = subprocess.run(["dbt", "run", "--profiles-dir", ".."], cwd="dbt_garmin_transformation", check=True)
    return result

@flow(name="Garmin ELT Pipeline")
def garmin_pipeline():

    ingest = run_ingestion()

    dbt = run_dtb(wait_for=[ingest])

if __name__ == "__main__":
    garmin_pipeline()

