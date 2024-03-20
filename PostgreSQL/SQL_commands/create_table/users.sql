CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullName VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- id|fullName        |email                       |
-- --+----------------+----------------------------+
--  1|Elizabeth Patton|alexandra80@example.net     |
--  2|Rodney Craig    |pjohnson@example.net        |
--  3|Paul Daniel     |xjohnson@example.org        |
--  4|Amanda Parks    |clintongraham@example.com   |
--  5|Joseph Patterson|yhoward@example.org         |
--  6|Timothy Jimenez |davenportdorothy@example.net|
--  7|James Moreno    |lukeroberts@example.org     |