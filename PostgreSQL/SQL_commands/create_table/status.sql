CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    CONSTRAINT valid_status_name CHECK (name IN ('new', 'in progress', 'completed'))
);


-- id|name       |
-- --+-----------+
--  1|new        |
--  2|in progress|
--  3|completed  |