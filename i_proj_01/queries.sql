USE bright_ideas;

SELECT * FROM users;

SELECT * FROM ideas;

ALTER TABLE users MODIFY COLUMN alias VARCHAR(16) AFTER l_name;