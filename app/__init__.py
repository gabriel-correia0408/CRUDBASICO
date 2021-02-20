from flask import Flask
from flask_migrate import Migrate

from app.model import configure as config_db, db
from .sererializer import configure as config_ma


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\gabriel.correia\\Desktop\\CRUDBASICO\\crudebasico.db'
    app.config['QLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, db)

    from .books import bp_books
    app.register_blueprint(bp_books)

    return app
