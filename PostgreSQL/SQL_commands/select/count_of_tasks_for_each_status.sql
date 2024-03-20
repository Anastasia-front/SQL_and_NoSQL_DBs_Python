SELECT status_id, COUNT(*) AS task_count FROM tasks GROUP BY status_id;

-- status_id|task_count|
-- ---------+----------+
--         3|         4|
--         2|         3|
--         1|        10|
