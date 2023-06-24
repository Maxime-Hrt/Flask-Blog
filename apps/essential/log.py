from flask import Blueprint, render_template, request, session, flash, redirect, url_for, current_app

log = Blueprint("log", __name__, static_folder="static", template_folder="templates")


@log.route('/')
@log.route('/home')
def index():  # put application's code here
    with current_app.app_context():
        return render_template("layouts/home.html")


@log.route('/login', methods=['POST', 'GET'])
def login():
    with current_app.app_context():
        if request.method == "POST":
            session.permanent = True
            usr = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]

            session["username"] = usr
            session["password"] = password
            session["email"] = email

            flash("Login Successful")
            return redirect(url_for("log.users.user"))

        else:
            if "username" in session and "password" in session:
                flash("Already logged in!")
                return redirect(url_for("log.users.user"))

            return render_template("layouts/login.html")


@log.route("/logout")
def logout():
    with current_app.app_context():
        if "username" in session:
            usr = session["username"]
            flash(f"Thank {usr}, see you!", "info")
        session.pop("user", None)
        session.pop("password", None)
        return redirect(url_for("log.login"))
