from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import os
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

BRONZE_PATH = "/opt/airflow/data_lake/bronze/breweries.json"
SILVER_PATH = "/opt/airflow/data_lake/silver/"
GOLD_PATH = "/opt/airflow/data_lake/gold/aggregated_breweries.parquet"

def get_spark_session():
    return SparkSession.builder.appName("BreweryPipeline").getOrCreate()

def extract_api_data():
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(BRONZE_PATH), exist_ok=True)
        with open(BRONZE_PATH, "w") as f:
            json.dump(response.json(), f)
    else:
        raise Exception("Failed to fetch data from API")

def transform_to_silver():
    spark = get_spark_session()
    df = spark.read.json(BRONZE_PATH)
    df_clean = df.filter(col("state").isNotNull()).dropna(subset=["id", "name", "brewery_type", "state"])
    df_clean.write.mode("overwrite").partitionBy("state").parquet(SILVER_PATH)

def aggregate_to_gold():
    spark = get_spark_session()
    df = spark.read.parquet(SILVER_PATH)
    df_grouped = df.groupBy("state", "brewery_type").count()
    df_grouped.write.mode("overwrite").parquet(GOLD_PATH)

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='brewery_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    extract = PythonOperator(task_id='extract_api_data', python_callable=extract_api_data)
    silver = PythonOperator(task_id='transform_to_silver', python_callable=transform_to_silver)
    gold = PythonOperator(task_id='aggregate_to_gold', python_callable=aggregate_to_gold)
    extract >> silver >> gold
