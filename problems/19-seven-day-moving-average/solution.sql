-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT order_date, sales,
       ROUND(AVG(sales) OVER (ORDER BY order_date
                              ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS moving_avg_7day
FROM daily_traffic
ORDER BY order_date;
