ALTER TABLE tasks
ADD CONSTRAINT status_user_id_fkey
FOREIGN KEY (status_id)
REFERENCES status(id)
ON DELETE CASCADE;

-- Step 1: Drop foreign key constraints referencing the status table
-- Assuming there are foreign key constraints in the tasks table referencing the status_id column of the status table
-- ALTER TABLE tasks DROP CONSTRAINT status_id;

-- Step 2: Delete data from related tables
-- Assuming the tasks table has a status_id column referencing the id column of the status table
DELETE FROM tasks WHERE status_id IN (SELECT id FROM status);

-- Step 3: Drop the status table
DROP TABLE status CASCADE;

