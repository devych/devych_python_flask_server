from json import dump

from flask import Flask, jsonify
from app.db import test


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('env.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/hello')
    def hello():
        return jsonify(hello='world')

    @app.route('/dbtest')
    def db_test():
        data = test()
        return jsonify(data)

    return app
