"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding, Window.currentRow)
    return t["daily_sales"].withColumn("running_total", F.sum("sales").over(w)).orderBy("order_date")
