'''
@Author: your name
@Date: 2020-04-21 11:01:42
@LastEditTime: 2020-04-26 14:05:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/__init__.py
'''
import os
from flask import Flask
from ext import db

def create_app(test_config=None):
    # If option instance_relative_config is set true,
    # you should put your file in instance folder
    # which is in root folder of project.
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Load app configuration file if it exists, when not testing
        app.config.from_pyfile('config.py')
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initiate database for your app
    db.init_app(app)

    # Initiate APIs for your app
    @app.route('/hello')
    def hello():
        return 'Hello,world!'

    return app
