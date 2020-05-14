'''
@Author: your name
@Date: 2020-04-30 20:59:31
@LastEditTime: 2020-05-12 09:04:20
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/resources/auth.py
'''

# from flask import Blueprint
from flask_restful import Resource
# from flask_restful import fields, marshal_with
# from .. import model
# from flask import request
# from ..ext import db
# from flaskr import model
# from flask import request
# from flaskr.ext import db
# from sqlalchemy import text

# 定义parser

class Auth(Resource):
    '''
    Do your login, register, change password here
    '''
    def get(self):
        return "Good! You get here!"
