ALTER TABLE tasks
DROP CONSTRAINT tasks_user_id_fkey;

ALTER TABLE tasks
ADD CONSTRAINT tasks_user_id_fkey
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE;
