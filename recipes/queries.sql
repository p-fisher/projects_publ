USE recipes_users_schema;

SELECT * FROM users;

SELECT * FROM recipes;

INSERT INTO recipes (r_name,r_info,instructions,under30,last_made,created_at,user_id) VALUES ('cold soup','a no-frills way to a quick lunch','open a can of your favorite soup; eat it from th can at room temp','Yes','2022-02-15', NOW(), 1);

ALTER TABLE recipes RENAME COLUMN description TO r_info;

UPDATE recipes SET instructions = 'take a slice of white bread, dunk in water, slap onto a plate, and enjoy! garnish sparingly with corn niblets' WHERE id = 1;

ALTER TABLE recipes change under30 under30 varchar(3);

UPDATE recipes SET under30 = 'Yes' WHERE id = 1;

UPDATE recipes SET user_id = 1 WHERE id = 2;

UPDATE recipes SET
r_name='fried SPAM',
instructions='open a can of spam\r\n\r\ncut spam into quarter-inch slices\r\n\r\nheat in a skillet over low-medium heat\r\n\r\nflip after 5 minutes\r\n\r\nenjoy with mustard on bread, or as a standalone entree',
r_info='a bachelor staple!!',
under30='Yes',
last_made='2022-02-14',
updated_at=NOW(),
user_id='1'
WHERE ID=2;