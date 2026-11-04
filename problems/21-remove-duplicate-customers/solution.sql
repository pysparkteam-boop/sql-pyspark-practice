-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT customer_id, customer_name, email, phone
FROM (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY customer_name, email, phone ORDER BY customer_id) AS rn
    FROM customers
) d
WHERE rn = 1
ORDER BY customer_id;
