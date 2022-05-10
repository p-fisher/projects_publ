USE bright_ideas;

SELECT * FROM users;

SELECT * FROM ideas;

ALTER TABLE users MODIFY COLUMN alias VARCHAR(16) AFTER l_name;

INSERT INTO users (f_name,l_name,alias,email,pwd,created_at) VALUES ('Tom','Tiger','TomTiger','tom@tigerville.co','1234Tiger',NOW());