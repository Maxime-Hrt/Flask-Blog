from flask import Blueprint, session, render_template, current_app, request, flash, redirect, url_for
from database.db_article import get_articles, add_article, delete_article, get_article_by_date

users = Blueprint("users", __name__, static_folder="static", template_folder="templates")


@users.route('/', methods=['POST', 'GET'])
def user():
    with current_app.app_context():
        usr = session["username"]
        password = session["password"]
        email = session["email"]

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

    return render_template("layouts/new_post.html", title="", article_text="")


@users.route('/edit_article/<article_date>', methods=['POST', 'GET'])
def edit_article(article_date):
    print("KOKOKOK")
    print(article_date)
    article = get_article_by_date(date_of_post=article_date)

    with current_app.app_context():
        if "username" in session:
            if request.method == "POST":
                username = session["username"]
                title = request.form["title"]
                content = request.form["content"]

                delete_article(date_of_post=article.date_of_post)

                add_article(username=username, title=title, content=content)

                flash("The article is posted")
                return redirect(url_for("log.users.article_view"))

    return render_template("layouts/new_post.html", title=article.title, article_text=article.content)


@users.route('/articles', methods=['POST', 'GET'])
def article_view():
    articles = get_articles(username=session["username"])

    if request.method == "POST":
        for article in articles:
            delete_key = "delete_"+str(article.date_of_post)
            edit_key = "edit_"+str(article.date_of_post)

            if edit_key in request.form:
                if edit_key == (request.form[edit_key]):
                    return redirect(url_for("log.users.edit_article", article_date=article.date_of_post))

            if delete_key in request.form:
                if delete_key == (request.form[delete_key]):
                    delete_article(date_of_post=article.date_of_post)
                    flash("The article is deleted")
                    return redirect(url_for("log.users.article_view"))

    return render_template("layouts/usr_articles.html", articles=articles)
