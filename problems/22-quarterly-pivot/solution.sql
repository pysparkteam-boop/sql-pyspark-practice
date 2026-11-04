-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT product_id,
       SUM(CASE WHEN quarter = 'Q1' THEN amount ELSE 0 END) AS Q1_sales,
       SUM(CASE WHEN quarter = 'Q2' THEN amount ELSE 0 END) AS Q2_sales,
       SUM(CASE WHEN quarter = 'Q3' THEN amount ELSE 0 END) AS Q3_sales,
       SUM(CASE WHEN quarter = 'Q4' THEN amount ELSE 0 END) AS Q4_sales
FROM sales
GROUP BY product_id
ORDER BY product_id;
