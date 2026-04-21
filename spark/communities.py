import os
from pyspark.sql import SparkSession
from graphframes import GraphFrame

# =========================
# FIX WINDOWS (HADOOP)
# =========================
os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["hadoop.home.dir"] = "C:\\hadoop"

# =========================
# SPARK SESSION
# =========================
spark = SparkSession.builder \
    .appName("Social Network Communities") \
    .config("spark.jars", r"C:\spark-jars\graphframes-0.8.3-spark3.5-s_2.12.jar") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# =========================
# LOAD DATA
# =========================
edges_df = spark.read.csv(
    "../data/facebook_combined.txt",
    sep=" ",
    inferSchema=True
).toDF("src", "dst")

# =========================
# CREATE VERTICES
# =========================
vertices_df = edges_df.select("src") \
    .union(edges_df.select("dst")) \
    .distinct() \
    .withColumnRenamed("src", "id")

# =========================
# CREATE GRAPH
# =========================
g = GraphFrame(vertices_df, edges_df)

print("========== GRAPH INFO ==========")
print("Nodes:", g.vertices.count())
print("Edges:", g.edges.count())

g.edges.show(5)
g.vertices.show(5)

# =========================
# COMMUNITY DETECTION
# =========================
print("========== COMMUNITY DETECTION ==========")

result = g.labelPropagation(maxIter=5)
result.show(10)

# =========================
# COMMUNITIES GROUPED
# =========================
communities = result.groupBy("label").count().orderBy("count", ascending=False)

print("========== COMMUNITIES ==========")
communities.show()

# =========================
# SHORTEST PATHS
# =========================
print("========== SHORTEST PATHS ==========")

paths = g.shortestPaths(landmarks=["0", "107", "348"])
paths.select("id", "distances").show(10)

# =========================
# EXPORT CSV
# =========================
print("✔ Exporting communities to CSV...")

os.makedirs("../data", exist_ok=True)

result.toPandas().to_csv("../data/communities.csv", index=False)

print("✔ Communities exported to ../data/communities.csv")

# =========================
# STOP SPARK
# =========================
spark.stop()