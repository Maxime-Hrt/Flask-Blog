from flask import Blueprint, session, render_template

users = Blueprint("users", __name__, static_folder="static", template_folder="templates")


@users.route('/', methods=['POST', 'GET'])
def user():
    usr = session["username"]
    password = session["password"]
    return render_template("layouts/user.html", username=usr, password=password)


@users.route('/new_post', methods=['POST', 'GET'])
def new_post():
    return render_template("layouts/new_post.html")
