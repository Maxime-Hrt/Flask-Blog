import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from database.db import mongo

from apps.essential.log import log
from apps.essential.users import users

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
app.secret_key = os.environ['SESSION_KEY']
app.config['MONGO_URI'] = os.environ['DB_URI']
mongo.init_app(app)

app.permanent_session_lifetime = timedelta(minutes=5)

log.register_blueprint(users, url_prefix="/user")
app.register_blueprint(log, url_prefix="/")


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
