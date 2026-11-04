"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.orderBy("order_date").rowsBetween(-6, 0)
    return (t["daily_traffic"]
            .withColumn("moving_avg_7day", F.round(F.avg("sales").over(w), 2))
            .orderBy("order_date"))
