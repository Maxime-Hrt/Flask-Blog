from flask import Blueprint, session, render_template, current_app
from database.db import get_all_users

data_view = Blueprint("data_view", __name__, static_folder='static', template_folder='templates')


@data_view.route("/")
def visualisation():
    user_list = get_all_users()
    return render_template("layouts/view.html", user_list=user_list)
