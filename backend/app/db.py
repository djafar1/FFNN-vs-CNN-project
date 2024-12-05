from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config.from_object('app.config')  # Load config from `config.py`
    db.init_app(app)
    return app
