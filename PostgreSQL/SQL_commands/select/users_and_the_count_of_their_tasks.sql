SELECT users.id, users.fullName, COUNT(tasks.id) AS task_count FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id;


-- id|fullName        |task_count|
-- --+----------------+----------+
--  9|John Downs      |         0|
--  3|Steven Jacobs   |         1|
--  5|Gabriel Kent    |         0|
--  4|John Green      |         1|
-- 10|Emily Rose      |         4|
--  6|Jimmy Cross     |         1|
--  2|Laurie Perez    |         1|
--  7|Blake Miller DDS|         5|
--  1|Mike Cook       |         3|
--  8|Jeffrey Fisher  |         1|