#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """ Create a route /status that return a JSON with 'status': 'ok'"""
    return jsonify({"status": "OK"})
