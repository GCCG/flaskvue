'''
@Author: your name
@Date: 2020-05-11 15:46:14
@LastEditTime: 2020-05-14 16:31:15
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


entity_type_fields = {
    'ID': fields.Integer(attribute='id'),
    '实体类名': fields.String(attribute='entity_type_name'),
    '实体类描述': fields.String(attribute='description')
}
entity_type_list = fields.List(fields.Nested(entity_type_fields))
entity_type_response = {
    'message': fields.String,
    'entity_type_list': entity_type_list
}
class EntityType(Resource):
    @marshal_with(entity_type_response, envelope='resource')
    def get(self):
        # Check if parameters exist, if not, set them None
        try:
            entity_type_id = request.args['entity_type_id']
        except BaseException:
            entity_type_id = None
        try:
            entity_type_name = request.args['entity_type_name']
        except BaseException:
            entity_type_name = None
        try:
            description = request.args['description']
        except BaseException:
            description = None
        # Search for entity types using given parameters
        results = model.EntityType.query.filter(
            model.EntityType.id == entity_type_id if entity_type_id is not None else text(''),
            model.EntityType.entity_type_name == entity_type_name if entity_type_name is not None else text(''),
            model.EntityType.description.like('%' + description + '%') if description is not None else text('')
        )

        return {'message': '', 'entity_type_list': results}

    def put(self):
        entity_type_name = request.form.get('entity_type_name')
        description = request.form.get('description')

        if entity_type_name is not None \
                and model.EntityType.query.filter_by(entity_type_name=entity_type_name).first() is not None:
            return {'message': 'Entity type with name %s already exists' % entity_type_name}
        else:
            entity_type = model.EntityType(entity_type_name=entity_type_name, description=description)
            db.session.add(entity_type)
            db.session.commit()
            return {'message': 'Entity type creation succeed!'}

    def delete(self):
        entity_type = model.EntityType.query.filter_by(id=request.form.get('entity_type_id')).first()

        db.session.delete(entity_type)
        db.session.commit()

        return {'message': 'Entity type deletion succeed!'}

    def post(self):
        entity_type_id = request.form.get('entity_type_id')
        entity_type_name = request.form.get('entity_type_name')
        description = request.form.get('description')

        entity_type = model.EntityType.query.filter_by(id=entity_type_id).first()
        if entity_type is not None:
            if entity_type.entity_type_name != entity_type_name and \
                    model.EntityType.query.filter_by(entity_type_name=entity_type_name).first() is not None:
                return {'message': 'Entity type with name %s already exists' % entity_type_name}
            else:
                entity_type.set_name(entity_type_name)
                entity_type.set_description(description)

                db.session.commit()

                return {'message': 'Entity Type update succeed!'}


entity_fields = {
    'ID': fields.Integer(attribute='id'),
    '实体名': fields.String(attribute='entity_name'),
    '实体类型': fields.String(attribute='entity_type.entity_type_name'),
    '实体类型ID': fields.Integer(attribute='entity_type_id'),
    '描述': fields.String(attribute='description')
}
entity_list = fields.List(fields.Nested(entity_fields))
entity_response = {
    'message': fields.String,
    'entity_list': entity_list
}
class Entity(Resource):
    @marshal_with(entity_response, envelope='resource')
    def get(self):
        try:
            entity_id = request.args['entity_id']
        except BaseException:
            entity_id = None
        try:
            entity_type_id = request.args['entity_type_id']
        except BaseException:
            entity_type_id = None
        try:
            description = request.args['description']
        except BaseException:
            description = None
        try:
            entity_name = request.args['entity_name']
        except BaseException:
            entity_name = None

        results = model.Entity.query.filter(
            model.Entity.id == entity_id if entity_id is not None else text(''),
            model.Entity.entity_type_id == entity_type_id if entity_type_id is not None else text(''),
            model.Entity.description == description if description is not None else text(''),
            model.Entity.entity_name == entity_name if entity_name is not None else text('')
        )

        return {'message': '', 'entity_list': results}


operation_fields = {
    'ID': fields.Integer(attribute='id'),
    '操作名': fields.String(attribute='operation_name'),
    '实体类型ID': fields.Integer(attribute='entity_type_id'),
    '描述': fields.String(attribute='description')
}
operation_list = fields.List(fields.Nested(operation_fields))
operation_response = {
    'message': fields.String,
    'operation_list': operation_list
}
class Operation(Resource):
    @marshal_with(operation_response, envelope='resource')
    def get(self):
        try:
            operation_id = request.args['operation_id']
        except BaseException:
            operation_id = None
        try:
            entity_type_id = request.args['entity_type_id']
        except BaseException:
            entity_type_id = None
        try:
            operation_name = request.args['operation_name']
        except BaseException:
            operation_name = None
        try:
            description = request.args['description']
        except BaseException:
            description = None

        results = model.Operation.query.filter(
            model.Operation.id == operation_id if operation_id is not None else text(''),
            model.Operation.entity_type_id == entity_type_id if entity_type_id is not None else text(''),
            model.Operation.operation_name == operation_name if operation_name is not None else text(''),
            model.Operation.description == description if description is not None else text('')
        )

        return {'message': '', 'operation_list': results}


privilege_fields = {
    'ID': fields.Integer(attribute='id'),
    '操作ID': fields.Integer(attribute='operation_id'),
    '操作名': fields.String(attribute='operation.operation_name'),
    '实体ID': fields.Integer(attribute='entity_id'),
    '实体名': fields.String(attribute='entity.entity_name')

}
privilege_list = fields.List(fields.Nested(privilege_fields))
privilege_response = {
    'message': fields.String,
    'privilege_list': privilege_list
}
class Privilege(Resource):
    @marshal_with(privilege_response, envelope='resource')
    def get(self):
        try:
            privilege_id = request.args['privilege_id']
        except BaseException:
            privilege_id = None
        try:
            operation_id = request.args['operation_id']
        except BaseException:
            operation_id = None
        try:
            entity_id = request.args['entity_id']
        except BaseException:
            entity_id = None

        results = model.Privilege.query.filter(
            model.Privilege.id == privilege_id if privilege_id is not None else text(''),
            model.Privilege.operation_id == operation_id if operation_id is not None else text(''),
            model.Privilege.entity_id == entity_id if entity_id is not None else text('')
        )

        return {'message': '', 'privilege_list': results}


group_fields = {
    'ID': fields.Integer(attribute='id'),
    '组名': fields.String(attribute='group_name'),
    '描述': fields.String(attribute='description')
}
group_list = fields.List(fields.Nested(group_fields))
group_response = {
    'message': fields.String,
    'group_list': group_list
}


role_fields = {
    "ID": fields.Integer(attribute='id'),
    "角色名": fields.String(attribute='role_name'),
    "描述": fields.String(attribute='description')
}
role_list = fields.List(fields.Nested(role_fields))
role_response = {
    "message": fields.String,
    "role_list": role_list
}


user_fields = {
    "ID": fields.Integer(attribute='id'),
    "用户名": fields.String(attribute='user_name'),
    "邮箱": fields.String(attribute='email'),
    "联系方式": fields.String(attribute='phone_number'),
    "所属用户组": fields.String(attribute='group.group_name'),
    '性别': fields.String(attribute='gender')
}
user_list = fields.List(fields.Nested(user_fields))
user_response = {
    "message": fields.String,
    "user_list": user_list
}


class Group(Resource):
    @marshal_with(group_response, envelope='resource')
    def get(self):
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
            group.set_group_name(group_name)
            group.set_description(description)
            db.session.commit()
            return {'message': 'Group edition succeed!'}
        else:
            return {'message': 'No group with id: %d' % group_id}

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
            # 检查修改后的名称是否存在重名
            if role.role_name != role_name and model.Role.query.filter_by(role_name=role_name).first() is not None:
                return {"message": "Another role with name %s already exists" % role_name}
            role.set_role_name(role_name)
            role.set_description(description)
            db.session.commit()

            return {"message": "Role update succeed"}
        else:
            return {"message": "No role with id: %d" % role_id}


group_roles_response = {
    'message': fields.String,
    '用户组ID': fields.Integer,
    '用户组名': fields.String,
    '用户组描述': fields.String,
    'role_list': role_list
}
class Group_Roles(Resource):
    @marshal_with(group_roles_response, envelope='resource')
    def get(self):
        try:
            group = model.Group.query.filter_by(id=request.args['group_id']).first()
            return {
                "message": '',
                "role_list": group.roles,
                '用户组ID': group.id,
                '用户组名': group.group_name,
                '用户组描述': group.description
            }
        except BaseException:
            pass

        try:
            group = model.Group.query.filter_by(group_name=request.args['group_name']).first()
            return {
                "message": '',
                "role_list": group.roles,
                '用户组ID': group.id,
                '用户组名': group.group_name,
                '用户组描述': group.description
            }
        except BaseException:
            pass

    def post(self):
        pass


role_groups_response = {
    'message': fields.String,
    '角色ID': fields.Integer,
    '角色名': fields.String,
    '角色描述': fields.String,
    'group_list': group_list
}
class Role_Groups(Resource):
    @marshal_with(role_groups_response, envelope='resource')
    def get(self):
        try:
            role = model.Role.query.filter_by(id=request.args['role_id']).first()
            return {
                "message": '',
                "group_list": role.groups,
                '角色ID': role.id,
                '角色名': role.role_name,
                '角色描述': role.description
            }
        except BaseException:
            pass
        try:
            role = model.Role.query.filter_by(role_name=request.args['role_name']).first()
            return {
                "message": '',
                "group_list": role.groups,
                '角色ID': role.id,
                '角色名': role.role_name,
                '角色描述': role.description
            }
        except BaseException:
            pass

        return{'message': "Bad role_id or role_name!"}

    def post(self):
        pass


class User(Resource):
    @marshal_with(user_response, envelope='resource')
    def get(self):
        user_id = request.form.get('id')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        group_name = request.form.get('group_name')
        gender = request.form.get('gender')

        results = model.User.query.filter(
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
        user_id = request.form.get('id')
        user_name = request.form.get('user_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        group = model.Group.query.filter_by(group_name=request.form.get('group_name')).first()
        gender = request.form.get('gender')

        user = model.User.query.filter_by(id=user_id).first()
        if user is not None:
            if user_name != user.user_name and model.User.query.filter(user_name=user_name) is not None:
                return {"message": "User with name %s already exists" % user_name}
            else:
                user.set_user_name(user_name)
                user.set_email(email)
                user.set_phone_number(phone_number)
                user.set_group(group)
                user.set_gender(gender)
                db.session.commit()
