# BEES – Data Engineering Case: Breweries Pipeline

## 📌 Descrição

Este projeto implementa um pipeline de dados baseado em arquitetura Medallion (bronze, silver, gold), com orquestração via Apache Airflow e execução em ambiente Docker. A fonte de dados é a Open Brewery DB API, contendo informações públicas sobre cervejarias nos EUA.

## 🚀 Execução

Para rodar o projeto localmente:

```bash
docker-compose up --build
```

Acesse a interface do Airflow em: http://localhost:8080  
Usuário padrão: `airflow`  
Senha padrão: `airflow`

## 🏗️ Estrutura do Pipeline

1. **Bronze Layer**: Coleta os dados da API e salva em formato JSON, sem transformações.
2. **Silver Layer**: Converte os dados para formato Parquet, particionado por estado da cervejaria.
3. **Gold Layer**: Gera uma visão analítica com a contagem de cervejarias por tipo e estado.


## 📂 Estrutura do Data Lake

```
data_lake/
├── bronze/        -> Dados crus (JSON)
├── silver/        -> Dados em Parquet particionados por estado
└── gold/          -> Agregação de cervejarias por tipo e estado
```

## 📊 Resultado esperado

Após a execução do pipeline no Airflow, os arquivos transformados estarão salvos localmente na pasta `data_lake`, organizados por camada.

