'''
@Author: your name
@Date: 2020-04-29 16:39:27
@LastEditTime: 2020-05-12 08:45:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/__init__.py
'''

from . import app


def create_app(config_file=None):
    return app.create_app(config_file)
