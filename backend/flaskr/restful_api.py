# -*- coding: UTF-8 -*-
'''
@Author: your name
@Date: 2020-04-26 10:30:43
@LastEditTime: 2020-04-29 16:25:47
@LastEditors: Please set LastEditors
@Description: 在这里将应用的所有的API注册到APP
@FilePath: /backend/flaskr/migrations/api.py
'''

from flask_restful import Resource, Api
from flask_restful import fields, marshal_with
import model
from flask import request
from ext import db
from sqlalchemy import text


class Auth(Resource):
    '''
    Do your login, register, change password here
    '''
    pass


"""
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
 """

class EntityType(Resource):
    pass


class Entity(Resource):
    pass


class Operation(Resource):
    pass


class Privilege(Resource):
    pass


group_fields = {
    'ID': fields.Integer(attribute='id'),
    '组名': fields.String(attribute='group_name'),
    '描述': fields.String(attribute='description')
}


""" group_list = {
    fields.List(fields.Nested(group_fields))
} """

group_response = {
    'message': fields.String,
    'group_list': fields.List(fields.Nested(group_fields))
}

'''
class GroupList(Resource):
    @marshal_with(group_response, envelope='resource')
    def get(self, ):
        return {'message': '', 'group_list': model.Group.query.all()}
'''


class Group(Resource):
    @marshal_with(group_response, envelope='resource')
    def get(self,):
        # Access control code here

        group_id = request.form.get('id')
        group_name = request.form.get('group_name')
        description = request.form.get('description')
        results = model.Group.query.filter(
            model.Group.id == group_id if group_id is not None else text(''),
            model.Group.group_name == group_name if group_name is not None else text(''),
            model.Group.description.like("%" + description + "%") if description is not None else text('')
        )

        return {'message': 'group_id is %r' % group_id, 'group_list': results}

    def put(self):
        if request.form.get('group_name') is None:
            return {'message': 'group_name should not be empty!'}
        '''
        else:
            return {
                'message':
                'group_name is %s, description is %s' %
                (request.form.get('group_name'), request.form.get('description'))}
        '''
        if model.Group.query.filter(model.Group.group_name == request.form.get('group_name')).first() is not None:
            return {'message': 'group_name %s already exists!' % request.form.get('group_name')}
        group = model.Group(
            group_name=request.form.get('group_name'),
            description=request.form.get('description')
        )
        # return 'group_id is %d, group_name is %s, description is %s' % (group.id, group.group_name, group.description)

        db.session.add(group)
        db.session.commit()
        return {'message': 'Group creation succeed!'}

    def delete(self):
        group_id = request.form.get('id')

        group_obj = model.Group.query.filter(
            model.Group.id == group_id
        ).first()
        db.session.delete(group_obj)
        db.session.commit()
        return {'message': 'Group deletion succeed!'}

    def post(self):
        group_id = request.form.get('id')
        group_name = request.form.get('group_name')
        description = request.form.get('description')

        group = model.Group.query.filter_by(id=group_id).first()
        if group is not None:
            group.group_name = group_name
            group.description = description
            db.session.commit()
            return {'message': 'Group edition succeed!'}
        else:
            return {'message': 'No group with id: %d' % group_id}


class Role(Resource):
    def get(self):
        pass


class User(Resource):
    pass


def init_app(app):
    api = Api(app)
    # api.add_resource(HelloWorld, '/helloworld')
    # api.add_resource(GroupList, '/api/grouplist')
    api.add_resource(Group, '/api/group')
