-- 1. Total number of transactions
SELECT COUNT(*) AS total_transactions
FROM transactions;


-- 2. Total transaction amount
SELECT SUM(amount) AS total_amount
FROM transactions;


-- 3. Transactions by type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY transaction_type;


-- 4. Successful transactions
SELECT *
FROM transactions
WHERE status = 'SUCCESS';


-- 5. Failed transactions
SELECT *
FROM transactions
WHERE status = 'FAILED';


-- 6. Top 3 highest transactions
SELECT *
FROM transactions
ORDER BY amount DESC
LIMIT 3;


-- 7. Unique customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM transactions;