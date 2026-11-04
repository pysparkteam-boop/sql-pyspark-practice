-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT c.customer_id, c.customer_name, c.city, COUNT(o.order_id) AS order_count
FROM customer c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name, c.city
ORDER BY c.customer_id;
