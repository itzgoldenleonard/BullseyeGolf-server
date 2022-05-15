"""The main flask app for the BullseyeGolf backend."""

from flask import Flask
from flask_restful import Api
from .routes import initialize_routes
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from .database.db import initialize_db

def create_app(test_config=None):  # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    api = Api(app)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/bullseyegolf'
    }

    initialize_db(app)

    initialize_routes(api)

    return app

