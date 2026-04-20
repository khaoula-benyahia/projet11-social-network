import os

os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("test") \
    .master("local[*]") \
    .getOrCreate()

df = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "val"])
df.show()

print("Spark OK")

spark.stop()