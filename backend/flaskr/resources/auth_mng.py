'''
@Author: your name
@Date: 2020-05-11 15:46:14
@LastEditTime: 2020-05-13 10:03:37
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/resources/auth_mng.py
'''
# -*- coding: UTF-8 -*-

from flask_restful import Resource  # , Api
from flask_restful import fields, marshal_with
from .. import model
from flask import request
from ..ext import db
from sqlalchemy import text

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


group_response = {
    'message': fields.String,
    'group_list': fields.List(fields.Nested(group_fields))
}


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


role_fields = {
    "ID": fields.Integer(attribute='id'),
    "角色名": fields.String(attribute='role_name'),
    "描述": fields.String(attribute='description')
}
role_response = {
    "message": fields.String,
    "role_list": fields.List(fields.Nested(role_fields))
}

class Role(Resource):
    @marshal_with(role_response, envelope='resource')
    def get(self):
        role_id = request.form.get('id')
        role_name = request.form.get('role_name')
        description = request.form.get('description')

        results = model.Role.query.filter(
            model.Role.id == role_id if role_id is not None else text(''),
            model.Role.role_name == role_name if role_name is not None else text(''),
            model.Role.description.like("%" + description + "%") if description is not None else text('')
        )

        return {
            "message": 'Role name is: %s' % role_name,
            "role_list": results
        }

    def put(self):
        if request.form.get('role_name') is None:
            return {"message": "role_name should not be none"}

        role_name = request.form.get('role_name')
        description = request.form.get('description')
        if model.Role.query.filter(model.Role.role_name == role_name).first() is not None:
            return {"message": "role with name %s already exists!" % role_name}

        role = model.Role(
            role_name=role_name,
            description=description
        )

        db.session.add(role)
        db.session.commit()
        return {"message": "Role creation succeed"}

    def delete(self):
        role = model.Role.query.filter_by(id=request.form.get('id')).first()

        db.session.delete(role)
        db.session.commit()

        return {"message": "Role deletion succeed"}

    def post(self):
        role_id = request.form.get('id')
        role_name = request.form.get('role_name')
        description = request.form.get('description')

        role = model.Role.query.filter(role_id=role_id).first()
        if role is not None:
            role.role_name = role_name
            role.description = description
            db.session.commit()

            return {"message": "Role update succeed"}
        else:
            return {"message": "No role with id: %d" % role_id}


user_fields = {
    "ID": fields.Integer(attribute='id'),
    "用户名": fields.String(attribute='user_name'),
    "邮箱": fields.String(attribute='email'),
    "联系方式": fields.String(attribute='phone_number'),
    "所属用户组": fields.String(attribute='group.group_name'),
    '性别': fields.String(attribute='gender')
}


user_response = {
    "message": fields.String,
    "user_list": fields.List(fields.Nested(user_fields))
}


class User(Resource):
    def get(self):
        user_id = request.form.get('id')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        group_name = request.form.get('group_name')
        gender = request.form.get('gender')

        results = model.query.filter(
            model.User.id == user_id if user_id is not None else text(''),
            model.User.user_name == user_name if user_name is not None else text(''),
            model.User.email == email if email is not None else text(''),
            model.User.phone_number == phone_number if phone_number is not None else text(''),
            model.User.group.group_name == group_name if group_name is not None else text(''),
            model.User.gender == gender if gender is not None else text('')
        )

        return {
            "message": '',
            "user_list": results
        }

    def put(self):
        if request.form.get('user_name') is None or request.form.get('password') is None:
            return {"message": "user_name or password should not be empty"}

        user_name = request.form.get('user_name')
        if model.User.query.filter_by(user_name=user_name).first() is not None:
            return {"message": "User with name is already exists" % user_name}

        user = model.User(
            user_name=user_name,
            email=request.form.get('email'),
            phone_number=request.form.get('phone_number'),
            group=model.Group.query.filter_by(group_name=request.form.get('group_name')),
            gender=request.form.get('gender')
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User creation succeed"}

    def delete(self):
        user = model.User.query.filter_by(id=request.form.get('id')).first()
        if user is None:
            return {"message": "No user with id %d" % request.form.get('id')}

        db.session.delete(user)
        db.session.commit()

    def post(self):
        pass
