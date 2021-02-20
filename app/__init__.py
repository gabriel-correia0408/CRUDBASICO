from flask import Flask
from flask_migrate import Migrate
from app.model import configure as config_db, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\gabriel.correia\\Desktop\\CRUDBASICO\\crudebasico.db'
    app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False
    config_db(app)

    Migrate(app, db)
    return app
