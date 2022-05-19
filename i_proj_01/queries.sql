USE bright_ideas;

SELECT * FROM users;

SELECT * FROM ideas;

SELECT user_id FROM ideas;

ALTER TABLE users MODIFY COLUMN alias VARCHAR(16) AFTER l_name;

INSERT INTO users (f_name,l_name,alias,email,pwd,created_at) VALUES ('Tom','Tiger','TomTiger','tom@tigerville.co','1234Tiger',NOW());

INSERT INTO ideas (summary, created_at, user_id) VALUES ('here is a lengthy enough idea i came up with to test',NOW(),1);

SELECT * FROM likes;

DELETE FROM likes WHERE id IN (5,6);

DELETE FROM ideas WHERE id BETWEEN 15 AND 18;
DELETE FROM ideas WHERE id = 18;
commit;


INSERT INTO likes (user_id, idea_id) VALUES (4,15);

SELECT COUNT(*) FROM likes WHERE idea_id = 7;

SELECT * FROM likes LEFT JOIN users ON likes.user_id = users.id LEFT JOIN ideas ON likes.idea_id = ideas.id WHERE ideas.id = 15;

SELECT * FROM likes LEFT JOIN users ON likes.user_id = users.id LEFT JOIN ideas ON likes.idea_id = ideas.id LEFT JOIN users AS creator ON ideas.user_id = creator.id WHERE ideas.id = 15;

## tinkering with count on join queries for like counts
#SELECT COUNT(*) FROM likes WHERE (SELECT * FROM ideas LEFT JOIN users ON ideas.user_id=users.id LEFT JOIN likes ON likes.idea_id = ideas.id);

SELECT * FROM ideas LEFT JOIN users ON ideas.user_id=users.id LEFT JOIN (SELECT user_id, COUNT(*) AS like_count FROM likes) ON likes_count.id = ideas.id;

##more tinkering
SELECT i.user_id,i.summary,u.f_name,u.l_name,u.alias from ideas AS i JOIN users as u ON i.user_id=u.id;

rollback;

SET FOREIGN_KEY_CHECKS=0;
DELETE FROM ideas WHERE id = 15;
SELECT * FROM ideas;
