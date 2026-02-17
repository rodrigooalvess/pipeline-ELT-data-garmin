# 🏃‍♂️ Garmin Data Pipeline: De Dados Brutos a Insights de Performance

Este projeto é uma solução completa de **ELT (Extract, Load, Transform)** projetada para automatizar a ingestão e análise de dados de atividades físicas exportadas do Garmin. O pipeline transforma arquivos CSV brutos em uma camada analítica pronta para BI, utilizando as boas práticas de Engenharia de Dados.



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
```

---

## 🗺️ Roadmap de Evolução

Este projeto está em desenvolvimento contínuo. As próximas etapas planejadas para a evolução da arquitetura são:

### 🟢 Fase 1: Visualização e BI (Em breve)
- [ ] Conectar a tabela `fct_treinos_diarios` ao **Power BI**.
- [ ] Criar dashboards de performance com KPIs de Pace Médio, Volume Semanal e Zonas de Frequência Cardíaca.

### 🟣 Fase 2: Inteligência Artificial e Feedback Automático 
- [ ] Implementar integração com LLMs para analisar os treinos e gerar feedbacks personalizados.
- [ ] Desenvolver modelos de Machine Learning para prever o tempo estimado de conclusão para distâncias específicas com base no histórico de treinos.
- [ ] Usar ML para identificar treinos com métricas fora do padrão que possam indicar fadiga ou risco de lesão.

### 🟡 Fase 3: Infraestrutura e Nuvem
- [ ] Migrar o banco de dados local para uma instância gerenciada na **Cloud (GCP ou AWS)**.
- [ ] Implementar o armazenamento de arquivos brutos em Buckets (S3/GCS) para simular um Data Lake real.
- [ ] Containerizar a aplicação utilizando **Docker** para facilitar o deploy.

### 🟠 Fase 4: Orquestração Avançada
- [ ] Avaliar a migração do Prefect para o **Apache Airflow** para gerenciar fluxos de dados mais complexos.
- [ ] Implementar monitoramento de **Data Quality** mais rigoroso com a biblioteca **Great Expectations**.

### 🔵 Fase 5: Interface do Usuário (SaaS)
- [ ] Desenvolver uma Web App para que outros usuários possam realizar o upload de seus CSVs e visualizar relatórios e feedbacks da IA instantaneamente.
