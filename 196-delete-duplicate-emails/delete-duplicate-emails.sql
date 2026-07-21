# Write your MySQL query statement below
DELETE p1
FROM Person p1, Person p2 #inner join table
WHERE p1.email = p2.email
AND p1.id > p2.id #delete the one with greater ID