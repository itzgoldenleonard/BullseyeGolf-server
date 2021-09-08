"""Just a test."""

from flask import Flask, request
from flask_cors import CORS
from dataclass import DB, read

app = Flask(__name__)
CORS(app)


@app.route('/user/<string:db_id>', methods=['GET', 'POST'])
def index(db_id):
    """Test the connection."""
    if request.method == 'GET':
        database = read(db_id)
        return database.serialize()

    elif request.method == 'POST':
        return 'Youve used POST'
