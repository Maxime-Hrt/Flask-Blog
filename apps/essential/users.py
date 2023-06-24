from flask import Blueprint, session, render_template, current_app, request, flash, redirect, url_for
from database.db import add_user
from database.db_article import get_all_article, add_article

users = Blueprint("users", __name__, static_folder="static", template_folder="templates")


@users.route('/', methods=['POST', 'GET'])
def user():
    with current_app.app_context():
        usr = session["username"]
        password = session["password"]
        email = session["email"]

        add_user(username=usr, password=password, email=email)

    return render_template("layouts/user.html", username=usr, password=password, email=email)


@users.route('/new_post', methods=['POST', 'GET'])
def new_post():
    with current_app.app_context():
        if "username" in session:
            if request.method == "POST":
                username = session["username"]
                title = request.form["title"]
                content = request.form["content"]

                add_article(username=username, title=title, content=content)

                flash("The article is posted")
                return redirect(url_for("log.users.article_view"))

    return render_template("layouts/new_post.html")


@users.route('/article', methods=['POST', 'GET'])
def article_view():
    articles = get_all_article()
    return render_template("layouts/usr_articles.html", articles=articles)
