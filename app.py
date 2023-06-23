from flask import Flask, render_template, redirect, request, url_for, session, flash
from datetime import timedelta
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']

app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
@app.route('/home')
def index():  # put application's code here
    return render_template("layouts/home.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        session.permanent = True
        usr = request.form["username"]
        password = request.form["pass"]
        session["username"] = usr
        session["password"] = password

        flash("Login Successful")
        return redirect(url_for("user"))

    else:
        if "username" in session and "password" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))

        return render_template("layouts/login.html")


@app.route('/user', methods=['POST', 'GET'])
def user():
    usr = session["username"]
    password = session["password"]
    return render_template("layouts/user.html", username=usr, password=password)


if __name__ == '__main__':
    app.run(debug=True)
