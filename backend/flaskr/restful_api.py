'''
@Author: your name
@Date: 2020-04-26 10:30:43
@LastEditTime: 2020-04-26 14:02:35
@LastEditors: Please set LastEditors
@Description: 在这里将应用的所有的API注册到APP里头
@FilePath: /backend/flaskr/migrations/api.py
'''

from flask_restful import Resource, Api

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


def init_app(app):
    api = Api(app)
    api.add_resource(HelloWorld, '/')
