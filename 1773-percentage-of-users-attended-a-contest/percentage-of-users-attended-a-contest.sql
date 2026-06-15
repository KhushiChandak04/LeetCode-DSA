SELECT
    r.contest_id,
    ROUND(
        COUNT(r.user_id) * 100.0 /
        (SELECT COUNT(*) FROM Users), 2) AS percentage #nested queries
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;