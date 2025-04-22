import pytest
from pyspark.sql import SparkSession
from pyspark.sql import Row

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("test").getOrCreate()

def test_transform_to_silver_logic(spark):
    data = [
        Row(id="1", name="Brew1", brewery_type="micro", state="Texas"),
        Row(id=None, name="Brew2", brewery_type="micro", state="Texas"),
        Row(id="3", name="Brew3", brewery_type="micro", state=None),
    ]
    df = spark.createDataFrame(data)

    df_clean = df.dropna(subset=["id", "name", "brewery_type", "state"])

    assert df_clean.count() == 1
    row = df_clean.collect()[0]
    assert row["id"] == "1"
    assert row["state"] == "Texas"
