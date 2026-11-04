-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT MAX(salary) AS second_highest_salary
FROM salaries
WHERE salary < (SELECT MAX(salary) FROM salaries);
