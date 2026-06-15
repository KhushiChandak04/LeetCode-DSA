# Write your MySQL query statement below
SELECT s.user_id,
    ROUND(IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0), 2) AS confirmation_rate #ifnull is when it returns 0 for no entries and and sum as we are adding up, count for total counting
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id