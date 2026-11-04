"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    region_totals = t["sales"].groupBy("region").agg(F.sum("amount").alias("total_sales"))
    return region_totals.orderBy(F.desc("total_sales"))
