SELECT * FROM users JOIN tasks ON users.id = tasks.user_id WHERE tasks.status_id = (SELECT id FROM status WHERE name = 'in progress');

-- id|fullName        |email                  |id|title                                        |description                                                                                                                |status_id|user_id|
-- --+----------------+-----------------------+--+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+---------+-------+
--  7|Blake Miller DDS|lewiseric@example.net  | 8|Range great detail always.                   |Yeah become computer. Value think performance drive name. Especially toward agree walk moment firm American many.          |        2|      7|
--  7|Blake Miller DDS|lewiseric@example.net  |14|Must score area real alone growth plan claim.|Bed difficult front voice. Statement can Congress painting sit.¶Vote wall it. Happen social glass small keep but keep cost.|        2|      7|
--  4|John Green      |davidtaylor@example.com|21|Wash the dish                                |Take it, wash it, dry it                                                                                                   |        2|      4|