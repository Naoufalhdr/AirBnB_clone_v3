#!/usr/bin/python3
""" Flask Application """
from os import getenv
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Close storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Handler for 404 errors that retutns JSON response """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """ Run the Flask server """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
