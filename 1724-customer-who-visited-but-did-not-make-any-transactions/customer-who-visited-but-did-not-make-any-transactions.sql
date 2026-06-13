# Write your MySQL query statement below
SELECT customer_id, 
    COUNT(*) AS count_no_trans #checks how many rows belongs to that customer
FROM Visits
LEFT JOIN Transactions
ON Visits.visit_id = Transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id; #puts all rows of that customer together