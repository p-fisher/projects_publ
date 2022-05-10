from flaskapp.config.mysqlconnection import connectToMySQL
import re	# the regex module
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PWD_REGEX = re.compile(r'^[?=.A-Z0-9][?=.0-9A-Z].{6,}$')

from flask import flash

class User:
    db = "recipes_users_schema"

    def __init__(self,data):
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.pwd = data['pwd']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls,data):
        query = "INSERT INTO users (f_name,l_name,email,pwd,created_at) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(pwd)s, NOW());"
        print(data)
        return connectToMySQL(cls.db).query_db(query,data)
        #return from db you get is just the id


    @classmethod
    def sign_in(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['f_name']) < 2:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(user['l_name']) < 2:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(user['pwd']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid= False
        # if not PWD_REGEX.match(user['pwd']):
        #     flash("Password must contain 1 cap, 1 num, and be 8+ characters long.","register")
        #     is_valid=False
        if user['pwd'] != user['p_check']:
            flash("Passwords don't match","register")
        return is_valid


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])


