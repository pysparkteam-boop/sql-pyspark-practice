"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    trimmed = F.trim(F.col("amount"))
    return (t["transactions"]
            .filter(trimmed.rlike(r"^-?[0-9]+(\.[0-9]+)?$"))
            .select("tx_id", "customer", trimmed.cast("decimal(12,2)").alias("amount"))
            .orderBy("tx_id"))
