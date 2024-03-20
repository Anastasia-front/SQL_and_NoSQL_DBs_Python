-- UPDATE users SET fullName = 'New Name' WHERE id = <user_id>;


UPDATE users SET fullName = 'John Green' WHERE id = 4;
UPDATE users SET fullName = 'Mike Cook' WHERE id = 1;
UPDATE users SET fullName = 'Emily Rose' WHERE id = 10;

-- id|fullName        |email                    |
-- --+----------------+-------------------------+
--  2|Laurie Perez    |bobby21@example.org      |
--  3|Steven Jacobs   |robertcruz@example.net   |
--  5|Gabriel Kent    |tracymorgan@example.com  |
--  6|Jimmy Cross     |thompsonbrian@example.net|
--  7|Blake Miller DDS|lewiseric@example.net    |
--  8|Jeffrey Fisher  |mathew72@example.net     |
--  9|John Downs      |matthew53@example.org    |
--  4|John Green      |davidtaylor@example.com  |
--  1|Mike Cook       |bryantteresa@example.org |
-- 10|Emily Rose      |juliehoward@example.net  |