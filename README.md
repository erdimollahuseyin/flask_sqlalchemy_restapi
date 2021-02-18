# REST API With Flask & SQL Alchemy

Books API using Python Flask, SQL Alchemy and Marshmallow.

## Quick Start

```
$ git clone git@github.com:erdimollahuseyin/flask_sqlalchemy_restapi.git
$ cd flask_sqlalchemy_restapi/

# Activate venv
$ pip3 install virtualenv
$ virtualenv book_env
$ cd book_env
$ source bin/activate

# Install dependencies
$ cd ..
$ pip install -r requirements/base.pip

# Create DB
$ python
>> from book.crud.database import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python run.py

```
## Endpoints

- `GET`: /book
- `GET`: /book/:id
- `POST`: /book
- `PUT`: /book/:id
- `DELETE`: /book/:id
