"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    s = t["salaries"]
    top = s.agg(F.max("salary")).collect()[0][0]
    return s.filter(F.col("salary") < F.lit(top)).agg(F.max("salary").alias("second_highest_salary"))
