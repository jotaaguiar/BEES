
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializar sessão Spark
spark = SparkSession.builder.appName("BreweryPipeline").getOrCreate()

# Caminhos
bronze_path = "/opt/airflow/data_lake/bronze/breweries.json"
silver_path = "/opt/airflow/data_lake/silver/"
gold_path = "/opt/airflow/data_lake/gold/aggregated_breweries.parquet"

# Bronze → Silver
df = spark.read.json(bronze_path)

df_silver = (
    df
    .filter(col("state").isNotNull())
    .dropna(subset=["id", "name", "brewery_type", "state"])
    .select(
        "id", "name", "brewery_type", "street", "city", "state",
        "postal_code", "country", "longitude", "latitude", "phone", "website_url"
    )
)

df_silver.write.mode("overwrite").partitionBy("state").parquet(silver_path)

# Silver → Gold
df_gold = df_silver.groupBy("state", "brewery_type").count()
df_gold.write.mode("overwrite").parquet(gold_path)

spark.stop()
