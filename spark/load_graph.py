from pyspark.sql import SparkSession

# 1. Spark session
spark = SparkSession.builder \
    .appName("Facebook Graph") \
    .getOrCreate()

# 2. Charger les edges
edges_df = spark.read.csv(
    "../data/facebook_combined.txt",
    sep=" ",
    inferSchema=True
).toDF("src", "dst")

# 3. Créer les vertices
vertices_df = edges_df.select("src") \
    .union(edges_df.select("dst")) \
    .distinct() \
    .toDF("id")

# 4. Vérification
print("Nodes:", vertices_df.count())
print("Edges:", edges_df.count())

edges_df.show(5)
vertices_df.show(5)