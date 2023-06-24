from flask_pymongo import PyMongo
from datetime import datetime

mongo = PyMongo()


class User:
    def __init__(self, username, email, password, date_of_creation=None):
        self.username = username
        self.email = email
        self.password = password
        self.date_of_creation = date_of_creation or datetime.now()
        self.articles = []

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'date_of_creation': self.date_of_creation,
            'articles': self.articles
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            date_of_creation=data.get('date_of_creation'),
            # articles=data.get('articles', [])
        )


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    mongo.db.Users.insert_one(user.to_dict())


def get_all_users():
    users = mongo.db.Users.find()
    return [User.from_dict(user_data) for user_data in users]
