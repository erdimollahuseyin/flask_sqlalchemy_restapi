from .database import ma


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
