"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["employees"]
            .groupBy("department")
            .agg(F.round(F.avg("salary"), 2).alias("avg_salary"))
            .orderBy(F.desc("avg_salary")))
