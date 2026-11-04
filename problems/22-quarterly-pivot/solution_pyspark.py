"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    q = ["Q1", "Q2", "Q3", "Q4"]
    p = t["sales"].groupBy("product_id").pivot("quarter", q).agg(F.sum("amount")).fillna(0)
    return p.select("product_id", *[F.col(x).alias(x + "_sales") for x in q]).orderBy("product_id")
