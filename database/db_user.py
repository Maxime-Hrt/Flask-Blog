from flask_pymongo import PyMongo
from datetime import datetime
from flask import flash

mongo = PyMongo()


class User:
    def __init__(self, username, email, password, date_of_creation=None):
        self.username = username
        self.email = email
        self.password = password
        self.date_of_creation = date_of_creation or datetime.now()

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'date_of_creation': self.date_of_creation,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            date_of_creation=data.get('date_of_creation'),
        )


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    mongo.db.Users.insert_one(user.to_dict())


def get_all_users():
    users = mongo.db.Users.find()
    return [User.from_dict(user_data) for user_data in users]


def user_login(username, password):
    user = mongo.db.Users.find_one({'username': username})
    if user:
        if user["password"] == password:
            return User.from_dict(user)
        else:
            flash("Incorrect password")
    else:
        flash("Incorrect username")

    return None


def verify_double(username, email):
    """
    user = mongo.db.Users.find_one({'username': username})
    if user:
        return True
    else:
        return False
    """
    return bool(mongo.db.Users.find_one({'username': username}) or
                bool(mongo.db.Users.find_one({'email': email})))  # Return True if a user or an email is found

