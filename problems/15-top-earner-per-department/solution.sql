-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT emp_id, emp_name, department, salary
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC, emp_id) AS rn
    FROM employees_wf
) ranked
WHERE rn = 1
ORDER BY department;
