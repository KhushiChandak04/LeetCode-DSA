# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1 #creates today copy
JOIN Weather w2 #creates yesterday copy
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 #differece b/w the dates is 1
WHERE w1.temperature > w2.temperature;