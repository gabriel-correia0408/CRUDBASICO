from flask import Flask
from .model import configure as config_db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crudzin.db'
    config_db(app)
    return app
