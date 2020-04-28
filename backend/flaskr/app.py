'''
@Author: your name
@Date: 2020-04-21 11:01:42
@LastEditTime: 2020-04-27 16:54:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/__init__.py
'''
import os
from flask import Flask
from ext import db
from model import Group
import restful_api

def create_app(test_config=None, need_db=0):
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
    restful_api.init_app(app)

    @app.route('/hello')
    def hello():
        return 'Hello,world!'

    @app.route('/')
    def todo():
        # admin_group = Group(group_name='admin', description='Superuser of this system')
        # b.session.add(admin_group)
        # db.session.commit()

        admin = Group.query.filter_by(group_name='admin').first()
        '''
        return {'id': admin.id,
                'group_name': admin.group_name,
                'description': admin.description,
                'Tom': [1, 2, 3, 4, 5]}
        '''
        return admin.jsonify()

    if need_db == 0:
        return app
    elif need_db == 1:
        return app, db
