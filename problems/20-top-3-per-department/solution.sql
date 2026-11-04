-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT department_id, employee_id, first_name, salary
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk <= 3
ORDER BY department_id, salary DESC, employee_id;
