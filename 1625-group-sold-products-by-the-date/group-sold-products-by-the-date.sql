# Write your MySQL query statement below
SELECT sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products #to sort lexicographically
FROM Activities
GROUP BY sell_date #asked in que to do so
ORDER BY sell_date