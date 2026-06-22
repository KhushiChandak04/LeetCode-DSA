# Write your MySQL query statement below
SELECT customer_id 
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*) #here we select unique products from prod table
    FROM Product
)