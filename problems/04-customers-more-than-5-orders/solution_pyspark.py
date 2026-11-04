"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["customers"].join(t["orders"], "customer_id")
            .groupBy("customer_id", "customer_name")
            .agg(F.count("*").alias("order_count"))
            .filter(F.col("order_count") > 5)
            .orderBy(F.desc("order_count")))
