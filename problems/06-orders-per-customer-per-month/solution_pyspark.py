"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["sales"]
            .withColumn("month", F.trunc("order_date", "month"))
            .groupBy("customer_id", "month")
            .agg(F.count("*").alias("order_count"))
            .orderBy("customer_id", "month"))
