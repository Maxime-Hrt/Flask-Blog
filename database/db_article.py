from database.db_user import mongo
from datetime import datetime


class Article:
    def __init__(self, username, title, content, date_of_post=None):
        self.username = username
        self.title = title
        self.content = content
        self.date_of_post = date_of_post or datetime.now()

    def to_dict(self):
        return {
            'username': self.username,
            'title': self.title,
            'content': self.content,
            'date_of_post': self.date_of_post
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            title=data.get('title'),
            content=data.get('content'),
            date_of_post=data.get('date_of_post')
        )


def add_article(username, title, content):
    article = Article(username=username, title=title, content=content)
    mongo.db.Articles.insert_one(article.to_dict())


def get_all_article():
    articles = mongo.db.Articles.find()
    return [Article.from_dict(article_data) for article_data in articles]
