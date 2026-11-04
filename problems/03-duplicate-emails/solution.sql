-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT email, COUNT(*) AS count
FROM users
GROUP BY email
HAVING COUNT(*) > 1
ORDER BY email;
