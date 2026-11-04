"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    return (t["employees"]
            .groupBy(F.year("hire_date").alias("hire_year"))
            .agg(F.count("*").alias("hire_count"))
            .orderBy("hire_year"))
