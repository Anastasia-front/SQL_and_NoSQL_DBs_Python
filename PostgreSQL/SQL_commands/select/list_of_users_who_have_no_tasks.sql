SELECT * 
FROM users 
WHERE NOT EXISTS (
    SELECT 1 
    FROM tasks 
    WHERE tasks.user_id = users.id
);

-- id|fullName    |email                  |
-- --+------------+-----------------------+
--  5|Gabriel Kent|tracymorgan@example.com|
--  4|Brad Burton |davidtaylor@example.com|
--  9|John Downs  |matthew53@example.org  |

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);


-- id|fullName    |email                  |
-- --+------------+-----------------------+
--  4|Brad Burton |davidtaylor@example.com|
--  5|Gabriel Kent|tracymorgan@example.com|
--  9|John Downs  |matthew53@example.org  |
