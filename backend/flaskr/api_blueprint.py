'''
@Author: your name
@Date: 2020-05-09 08:40:53
@LastEditTime: 2020-05-12 08:56:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/api_blueprint.py
'''
from .resources.auth import Auth
from .resources.auth_mng import Group
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)
api.add_resource(Auth, '/auth')
api.add_resource(Group, '/group')
