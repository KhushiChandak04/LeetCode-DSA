# Write your MySQL query statement below
SELECT DISTINCT author_id AS id #as auth id appears multiple times, we use distinct and rename it as id as told
FROM Views
WHERE author_id = viewer_id #to chk if they have read their own article
ORDER BY id ASC #in ascending order