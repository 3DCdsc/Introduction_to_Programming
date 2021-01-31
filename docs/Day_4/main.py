from flask import Flask
import pyrebase
import json

app = Flask(__name__)

config = {
    "apiKey": "API KEY",
    "authDomain": "AUTH DOMAIN",
    "databaseURL": "DATABASE_URL"
}


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/books', methods=["GET"])
def get_books():
    """
    This endpoint returns all books from firebase

    If specified, available filters:
    - title
    - category
    """
    return 'These are all my books'


@app.route('/upload-books', methods=["POST"])
def upload_book():
    """
    This endpoint takes in a book via FormData and writes it to firebase.
    Returns the Book object
    """
    return


if __name__ == "__main__":
    app.run(debug=True)
