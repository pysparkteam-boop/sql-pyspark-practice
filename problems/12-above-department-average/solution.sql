-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.employee_id, e.first_name, e.salary, e.department_id
FROM employees e
JOIN dept_avg d ON d.department_id = e.department_id
WHERE e.salary > d.avg_salary
ORDER BY e.salary DESC;
