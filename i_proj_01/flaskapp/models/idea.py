from flaskapp.config.mysqlconnection import connectToMySQL
# import re	# the regex module
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PWD_REGEX = re.compile(r'^[?=.A-Z0-9][?=.0-9A-Z].{6,}$')

from flask import flash

class Idea:
    db = "bright_ideas"

    def __init__(self,data):
        self.id = data['id']
        self.id = data['user_id']
        self.id = data['idea_summ']
        # self.id = data['summary']
        # self.r_name = data['r_name']
        # self.instructions = data['instructions']
        # self.r_info = data['r_info']
        # self.under30 = data['under30']
        # self.last_made = data['last_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_idea(cls,data):
        query = "INSERT INTO ideas (idea_summ, created_at, user_id) VALUES (%(idea_summ)s, NOW(), %(user_id)s);"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def update(cls,data):
        # query = "UPDATE ideas SET r_name,instructions,r_info,under30,last_made,updated_at,user_id = %(r_name)s, %(instructions)s, %(r_info)s, %(under30)s, %(last_made)s, NOW(),'1';"
        query = "UPDATE ideas SET r_name = %(r_name)s, instructions = %(instructions)s, r_info = %(r_info)s, under30 = %(under30)s, last_made = %(last_made)s, updated_at = NOW() WHERE ID = %(id)s;"
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


    @staticmethod
    def validate_idea(idea):
        is_valid = True
        if len(idea['idea_summ']) < 50:
            is_valid = False
            flash("Idea should be more substantive! Add more content.","idea")
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






