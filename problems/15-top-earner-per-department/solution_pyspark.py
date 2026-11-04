"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.partitionBy("department").orderBy(F.desc("salary"), F.asc("emp_id"))
    return (t["employees_wf"]
            .withColumn("rn", F.row_number().over(w))
            .filter("rn = 1")
            .select("emp_id", "emp_name", "department", "salary")
            .orderBy("department"))
