from flask import Blueprint, render_template, request, session, flash, redirect, url_for, current_app
from database.db_user import user_login, verify_double, add_user

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
            usr = request.form["username"]
            password = request.form["password"]

            connected_user = user_login(usr, password)

            if connected_user:
                session.permanent = True
                session["username"] = usr
                session["password"] = password
                session["email"] = connected_user.email

                flash("Login Successful")
                return redirect(url_for("log.users.user"))

            else:
                render_template("layouts/login.html")

        else:
            if "username" in session and "password" in session:
                flash("Already logged in!")
                return redirect(url_for("log.users.user"))

    return render_template("layouts/login.html")


@log.route("/create_account", methods=['POST', 'GET'])
def create_account():
    with current_app.app_context():
        if request.method == 'POST':
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            password_conf = request.form["password_conf"]

            if not verify_double(username=username, email=email):
                if password == password_conf:
                    session.permanent = True
                    session["username"] = username
                    session["password"] = password
                    session["email"] = email

                    flash("Account successfully created")
                    add_user(username, email, password)
                    return redirect(url_for("log.users.user"))
                else:
                    flash("Both password are different")

            else:
                flash("This Email or Username is already taken")

    return render_template("layouts/create_account.html")


@log.route("/logout")
def logout():
    with current_app.app_context():
        if "username" in session:
            usr = session["username"]
            flash(f"Thank {usr}, see you!", "info")
            session.pop("username", None)
            session.pop("password", None)
            session.pop("email", None)
        else:
            flash("You are not logged in!")

        return redirect(url_for("log.login"))
