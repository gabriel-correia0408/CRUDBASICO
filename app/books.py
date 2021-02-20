from flask import Blueprint

bp_books = Blueprint('books', __name__)


@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
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
