SELECT * FROM users WHERE email LIKE '%@example.com';

-- id|fullName    |email                  |
-- --+------------+-----------------------+
--  4|Brad Burton |davidtaylor@example.com|
--  5|Gabriel Kent|tracymorgan@example.com|

SELECT * FROM users WHERE email LIKE '%@example.net';

-- id|fullName        |email                    |
-- --+----------------+-------------------------+
--  3|Steven Jacobs   |robertcruz@example.net   |
--  6|Jimmy Cross     |thompsonbrian@example.net|
--  7|Blake Miller DDS|lewiseric@example.net    |
--  8|Jeffrey Fisher  |mathew72@example.net     |
-- 10|Joanne Williams |juliehoward@example.net  |


SELECT * FROM users WHERE email LIKE '%@example.org';

-- id|fullName       |email                   |
-- --+---------------+------------------------+
--  1|Susan Alexander|bryantteresa@example.org|
--  2|Laurie Perez   |bobby21@example.org     |
--  9|John Downs     |matthew53@example.org   |
