# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS total_weight #computes total running weight of ppl in order
    FROM Queue
) q
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1 #takes onli 1 person in the list