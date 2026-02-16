# 🏃‍♂️ Garmin Data Pipeline: De Dados Brutos a Insights de Performance

Este projeto é uma solução completa de **ELT (Extract, Load, Transform)** projetada para automatizar a ingestão e análise de dados de atividades físicas exportadas do Garmin. O pipeline transforma arquivos CSV brutos em uma camada analítica pronta para BI, utilizando as melhores práticas de Engenharia de Dados.



## 🎯 Objetivo
Automatizar o processamento de métricas de corrida (Pace, Distância, FC), garantindo a qualidade dos dados através de testes automatizados e orquestração profissional com Prefect.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13+
* **Gerenciamento de Dependências:** Poetry
* **Banco de Dados:** PostgreSQL
* **Transformação de Dados:** dbt (Data Build Tool)
* **Orquestração:** Prefect
* **Qualidade:** dbt-tests

---

## 🏗️ Arquitetura de Dados
O projeto segue a arquitetura medalhão:
1.  **Landing:** Arquivos CSV brutos recebidos na pasta `data/landing`.
2.  **Raw (Bronze):** Dados ingeridos via Python sem transformações no schema `raw`.
3.  **Analytics (Silver/Gold):** Dados limpos, tipados e agregados via dbt no schema `analytics`.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
* PostgreSQL instalado localmente.
* Poetry instalado (`pip install poetry`).

### 2. Configuração do Banco de Dados
No seu PostgreSQL, crie um banco de dados e os schemas necessários:
```sql
CREATE DATABASE garmin_db;

-- Conecte ao banco e crie os schemas
CREATE SCHEMA raw;
CREATE SCHEMA analytics;
```

### 3. Execução do Pipeline
Para processar os dados, insira seus arquivos `.csv` na pasta `data/landing` e execute o comando:

> **Dica:** Já deixei um arquivo de exemplo dentro da pasta `data/landing` para que você possa testar o pipeline imediatamente! 🚀

```bash
poetry run python main.py