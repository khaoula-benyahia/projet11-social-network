from pyspark.sql import SparkSession
from graphframes import GraphFrame

# Création de Spark
spark = SparkSession.builder \
    .appName("Propagation") \
    .config("spark.jars", "file:///C:/spark-jars/graphframes-0.8.3-spark3.5-s_2.12.jar") \
    .getOrCreate()

# Charger les données
edges_df = spark.read.csv("../data/facebook_combined.txt", sep=" ").toDF("src", "dst")

# Créer les sommets
vertices_df = edges_df.select("src").union(edges_df.select("dst")).distinct().toDF("id")

# Créer le graphe
g = GraphFrame(vertices_df, edges_df)

# =========================
# SHORTEST PATHS
# =========================
print("========== SHORTEST PATHS ==========")

paths = g.shortestPaths(landmarks=["0", "107", "348"])
paths.select("id", "distances").show(10)