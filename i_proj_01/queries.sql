USE bright_ideas;

SELECT * FROM users;

SELECT * FROM ideas;

SELECT user_id FROM ideas;

ALTER TABLE users MODIFY COLUMN alias VARCHAR(16) AFTER l_name;

INSERT INTO users (f_name,l_name,alias,email,pwd,created_at) VALUES ('Tom','Tiger','TomTiger','tom@tigerville.co','1234Tiger',NOW());

INSERT INTO ideas (summary, created_at, user_id) VALUES ('here is a lengthy enough idea i came up with to test',NOW(),1);

select * from likes;

INSERT INTO likes (user_id, idea_id) VALUES (3,7);

SELECT COUNT(*) FROM likes WHERE idea_id = 7;