# Write your MySQL query statement below
SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%' #AFTER
OR conditions LIKE '% DIAB1%' #before, but preceeded by a space