"""Reference PySpark solution. `t` maps table name -> DataFrame."""
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def solve(t):
    w = Window.partitionBy("department_id").orderBy(F.desc("salary"))
    return (t["employees"]
            .withColumn("rnk", F.rank().over(w))
            .filter("rnk <= 3")
            .select("department_id", "employee_id", "first_name", "salary")
            .orderBy("department_id", F.desc("salary"), "employee_id"))
