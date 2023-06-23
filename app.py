from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv
from pathlib import Path
from apps.essential.log import log
from apps.essential.users import users
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']

app.permanent_session_lifetime = timedelta(minutes=5)

log.register_blueprint(users, url_prefix="/user")
app.register_blueprint(log, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True)
