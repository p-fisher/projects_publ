from flaskapp.config.mysqlconnection import connectToMySQL
# import re	# the regex module
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PWD_REGEX = re.compile(r'^[?=.A-Z0-9][?=.0-9A-Z].{6,}$')

from flask import flash
from flaskapp.models import user


class Idea:
    db = "bright_ideas"

    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.summary = data['summary']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.liked_by = []
        self.creator = None


    @classmethod
    def add_idea(cls,data):
        query = "INSERT INTO ideas (summary, created_at, user_id) VALUES (%(summary)s, NOW(), %(user_id)s);"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def update(cls,data):
        # query = "UPDATE ideas SET r_name,instructions,r_info,under30,last_made,updated_at,user_id = %(r_name)s, %(instructions)s, %(r_info)s, %(under30)s, %(last_made)s, NOW(),'1';"
        # query = "UPDATE ideas SET r_name = %(r_name)s, instructions = %(instructions)s, r_info = %(r_info)s, under30 = %(under30)s, last_made = %(last_made)s, updated_at = NOW() WHERE ID = %(id)s;"
        query="UPDATE ideas SET summary = %(summary)s, updated_at = NOW() WHERE ID = %(id)s;"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ideas WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ideas WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ideas;"
        results = connectToMySQL(cls.db).query_db(query)
        ideas = []
        for row in results:
            ideas.append(cls(row))
        return ideas


    @classmethod
    def get_ideas_with_users(cls):
        query = "SELECT * FROM ideas LEFT JOIN users ON ideas.user_id=users.id;"
        # query = "SELECT * FROM ideas LEFT JOIN users ON ideas.user_id=users.id LEFT JOIN likes ON likes.idea_id = ideas.id;"
        results = connectToMySQL(cls.db).query_db(query)
        # print(results)
        idea_list = []
        for row_from_db in results:
            idea_data = {
                "id": row_from_db['id'],
                "user_id": row_from_db['user_id'],
                "summary": row_from_db['summary'],
                "created_at": row_from_db['created_at'],
                "updated_at": row_from_db['updated_at']
            }
            new_idea = cls(idea_data)
            user_data = {
                "id": row_from_db["users.id"],
                "f_name": row_from_db["f_name"],
                "l_name": row_from_db["l_name"],
                "alias": row_from_db["alias"],
                "email": row_from_db["email"],
                "pwd": row_from_db['pwd'],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            new_idea.user = user.User(user_data)
            # new_idea.liked_by = user.User(user_data)
            idea_list.append(new_idea)
        return idea_list


    @classmethod
    def like_idea(cls, data):
        query = "INSERT INTO likes (user_id, idea_id) VALUES (%(user_id)s, %(idea_id)s);"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        return results



    @classmethod
    def read_idea_with_likes(cls, data):
        # query = "SELECT * FROM likes LEFT JOIN users ON likes.user_id = users.id LEFT JOIN ideas ON likes.idea_id = ideas.id WHERE ideas.id = %(id)s;"
        query = """
        SELECT * 
        FROM likes 
        LEFT JOIN users 
        ON likes.user_id = users.id 
        LEFT JOIN ideas 
        ON likes.idea_id = ideas.id 
        LEFT JOIN users AS creator 
        ON ideas.user_id = creator.id 
        WHERE ideas.id = %(id)s
        ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        print('^^^^^^^^^^^^^^^^', results)
        idea_data = {
            "id": results[0]['ideas.id'],
            "user_id": results[0]['user_id'],
            "summary": results[0]['summary'],
            "created_at": results[0]['created_at'],
            "updated_at": results[0]['updated_at']
        }
        creator_data = {
            "id": results[0]["creator.id"],
            "f_name": results[0]["creator.f_name"],
            "l_name": results[0]["creator.l_name"],
            "alias": results[0]["creator.alias"],
            "email": results[0]["creator.email"],
            "pwd": results[0]['creator.pwd'],
            "created_at": results[0]["creator.created_at"],
            "updated_at": results[0]["creator.updated_at"]
        }
        this_idea = cls(idea_data)
        for row in results:
            liker_data = {
                "id": row["users.id"],
                "f_name": row["f_name"],
                "l_name": row["l_name"],
                "alias": row["alias"],
                "email": row["email"],
                "pwd": row["pwd"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }
            this_idea.liked_by.append(user.User(liker_data))
            this_idea.creator = (user.User(creator_data))
        return this_idea


    @staticmethod
    def validate_idea(idea):
        is_valid = True
        if len(idea['summary']) < 30:
            is_valid = False
            flash("Ideas should be more substantive! Please use at least 30 characters.","idea")
        # if len(idea['instructions']) < 3:
        #     is_valid = False
        #     flash("Instructions must be 3 or more in length.","idea")
        # if len(idea['r_info']) < 3:
        #     is_valid = False
        #     flash("Description must be 3 or more in length (and less than 3000).","idea")
        # if idea['last_made'] == "":
        #     is_valid = False
        #     flash("Please enter a date","idea")
        # if idea['under30'] != "checked":                                        # how to do this?! also tried ==""
        #     is_valid = False
        #     flash("Please indicate if idea takes more/less than 30 minutes to complete.","idea") 
        return is_valid






