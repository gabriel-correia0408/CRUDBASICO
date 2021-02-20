from flask import Blueprint
from .model import Book
from .sererializer import BookSchema

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


@bp_books.route('/cadastrar', methods=['PUT'])
def cadastar():
    ...
