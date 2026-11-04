"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.partitionBy("department_id")
    return (t["employees"]
            .withColumn("dept_avg", F.avg("salary").over(w))
            .filter(F.col("salary") > F.col("dept_avg"))
            .select("employee_id", "first_name", "salary", "department_id")
            .orderBy(F.desc("salary")))
