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


def get_articles(username):
    articles = mongo.db.Articles.find({'username': username})
    return [Article.from_dict(article_data) for article_data in articles]


def get_article_by_date(date_of_post):
    article = mongo.db.Articles.find_one({'date_of_post': date_of_post})
    print(date_of_post)
    print("cacaca")
    print(article)
    if article:
        return Article.from_dict(article)
    else:
        return None


def delete_article(date_of_post):
    print(date_of_post)
    mongo.db.Articles.delete_one({'date_of_post': date_of_post})

