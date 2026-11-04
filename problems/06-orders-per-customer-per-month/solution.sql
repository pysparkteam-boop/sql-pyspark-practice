-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT customer_id,
       CAST(date_trunc('month', order_date) AS DATE) AS month,
       COUNT(*) AS order_count
FROM sales
GROUP BY customer_id, CAST(date_trunc('month', order_date) AS DATE)
ORDER BY customer_id, month;
