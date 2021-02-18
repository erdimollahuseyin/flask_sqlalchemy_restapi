from flask import Flask

app = Flask(__name__)

from book.crud import routes
