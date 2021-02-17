# REST API With Flask & SQL Alchemy

Books API using Python Flask, SQL Alchemy and Marshmallow.

## Quick Start

```
# Activate venv
$ pip3 install virtualenv
$ virtualenv book_env
$ cd book_env
$ source bin/activate

# Install dependencies
$ pip install -r requirements/base.pip

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py

```
## Endpoints

- `GET`: /book
- `GET`: /book/:id
- `POST`: /book
- `PUT`: /book/:id
- `DELETE`: /book/:id
