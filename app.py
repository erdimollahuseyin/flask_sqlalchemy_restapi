import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

# Init book_app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir, 'db.sqlite'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)


class Book(db.Model):
    """
    Book Class Model.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class BookSchema(ma.Schema):
    """
    Book Schema.
    """

    class Meta:
        strict = True
        fields = ('id', 'name', 'description', 'price')


# Init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)


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
    book = Book.query.get(id)

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


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
