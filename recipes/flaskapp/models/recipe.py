from flaskapp.config.mysqlconnection import connectToMySQL
# import re	# the regex module
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PWD_REGEX = re.compile(r'^[?=.A-Z0-9][?=.0-9A-Z].{6,}$')

from flask import flash

class Recipe:
    db = "recipes_users_schema"

    def __init__(self,data):
        self.id = data['id']
        self.r_name = data['r_name']
        self.instructions = data['instructions']
        self.r_info = data['r_info']
        self.under30 = data['under30']
        self.last_made = data['last_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes (r_name,instructions,r_info,under30,last_made,created_at,user_id) VALUES (%(r_name)s, %(instructions)s, %(r_info)s, %(under30)s, %(last_made)s, NOW(),'1');"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def update(cls,data):
        # query = "UPDATE recipes SET r_name,instructions,r_info,under30,last_made,updated_at,user_id = %(r_name)s, %(instructions)s, %(r_info)s, %(under30)s, %(last_made)s, NOW(),'1';"
        query = "UPDATE recipes SET r_name = %(r_name)s, instructions = %(instructions)s, r_info = %(r_info)s, under30 = %(under30)s, last_made = %(last_made)s, updated_at = NOW() WHERE ID = %(id)s;"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        print(results)
        return cls(results[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes




    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['r_name']) < 3:
            is_valid = False
            flash("Recipe name must be 3 or more in length.","recipe")
        if len(recipe['instructions']) < 3:
            is_valid = False
            flash("Instructions must be 3 or more in length.","recipe")
        if len(recipe['r_info']) < 3:
            is_valid = False
            flash("Description must be 3 or more in length (and less than 3000).","recipe")
        if recipe['last_made'] == "":
            is_valid = False
            flash("Please enter a date","recipe")
        # if recipe['under30'] != "checked":                                        # how to do this?! also tried ==""
        #     is_valid = False
        #     flash("Please indicate if recipe takes more/less than 30 minutes to complete.","recipe") 
        return is_valid






