"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["customer"].join(t["orders"], "customer_id", "left")
            .groupBy("customer_id", "customer_name", "city")
            .agg(F.count("order_id").alias("order_count"))
            .orderBy("customer_id"))
