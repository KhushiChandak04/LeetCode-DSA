# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count, #COUNTS ALL ROWS
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount #if(condition, value, 0) is the syntax
FROM Transactions
GROUP BY month, country