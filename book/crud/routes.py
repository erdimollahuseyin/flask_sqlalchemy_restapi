from flask import jsonify, request

from book import app

from .database import db
from .models import Book
from .schemas import book_schema, books_schema


@app.route('/book', methods=['POST'])
def add_book():
    """
    Create a book.
    """
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')

    new_book = Book(name, description, price)
    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)


@app.route('/book', methods=['GET'])
def get_books():
    """
    Get all books.
    """
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)


@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    """
    Get single books.
    """
    book = Book.query.get(id)
    return book_schema.jsonify(book)


@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
    """
    Update a book.
    """
    book = Book.query.get(id == id)

    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')

    book.name = name
    book.description = description
    book.price = price

    db.session.commit()

    return book_schema.jsonify(book)


@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    """
    Delete a book by id.
    """
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)
