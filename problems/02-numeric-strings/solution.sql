-- Reference solution (runs on DuckDB; see README for the MySQL variant if any)
SELECT tx_id,
       customer,
       CAST(TRIM(amount) AS DECIMAL(12,2)) AS amount
FROM transactions
WHERE regexp_matches(TRIM(amount), '^-?[0-9]+(\.[0-9]+)?$')
ORDER BY tx_id;
