"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["users"]
            .groupBy("email")
            .agg(F.count("*").alias("count"))
            .filter(F.col("count") > 1)
            .orderBy("email"))
