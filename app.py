"""Just a test."""
import json
from flask import Flask, request, Response
from flask_cors import CORS
import os
from dataclass import DB, read

app = Flask(__name__)
CORS(app)


@app.route('/user/<string:db_id>', methods=['GET', 'POST'])
def index(db_id):
    """Test the connection."""
    if request.method == 'GET':
        if db_id == "ALL":
            list_of_databases: str = "["
            for i in os.listdir('DB'):
                list_of_databases += (read(i).serialize()) + ', '

            list_of_databases = list_of_databases[:len(list_of_databases) - 2]  # remove the last ', '
            return Response(list_of_databases + ']', mimetype='text/json')
            # I'm turning it into a string to avoid double serializing it
            # REFACTOR: Manually JSON serializing is kinda janky, probably needs a refactoring

        else:
            database = read(db_id)
            return database.serialize()

    elif request.method == 'POST':
        database = read(db_id)
        if database.add_score(request.json['name'], request.json['score']) == -1:
            return {"error": 'invalid name'}, 400
        database.write()
        return 'OK', 200
