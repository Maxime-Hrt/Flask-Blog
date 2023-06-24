from flask import Blueprint, session, render_template, current_app
from database.db import add_user

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
        return render_template("layouts/new_post.html")
