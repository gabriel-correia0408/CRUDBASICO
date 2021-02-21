from flask import Blueprint, current_app, request

from app.model import Book
from app.sererializer import BookSchema

bp_books = Blueprint('books', __name__)


@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200
    ...


@bp_books.route('/deletar', methods=['DELETE'])
def deletar():
    ...


@bp_books.route('/modificar', methods=['PATCH'])
def modificar():
    ...
