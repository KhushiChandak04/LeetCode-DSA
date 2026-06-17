# Write your MySQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt #JUST ADD UNIQUE TEACHERS HERE
FROM Teacher
GROUP BY teacher_id