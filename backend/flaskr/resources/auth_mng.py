'''
@Author: your name
@Date: 2020-05-11 15:46:14
@LastEditTime: 2020-05-25 08:53:32
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
# from .auth import check_access_permission, check_auth_token


K_ENTITY_TYPE_ID = 'entity_type_id'
K_ENTITY_TYPE_NAME = 'entity_type_name'
K_ENTITY_TYPE_DESCRIPTION = 'description'
entity_type_fields = {
    K_ENTITY_TYPE_ID: fields.Integer(attribute='id'),
    K_ENTITY_TYPE_NAME: fields.String(attribute='entity_type_name'),
    K_ENTITY_TYPE_DESCRIPTION: fields.String(attribute='description')
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
            entity_type_id = request.args[K_ENTITY_TYPE_ID]
        except BaseException:
            entity_type_id = None
        try:
            entity_type_name = request.args[K_ENTITY_TYPE_NAME]
        except BaseException:
            entity_type_name = None
        try:
            description = request.args[K_ENTITY_TYPE_DESCRIPTION]
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
        entity_type_name = request.form.get(K_ENTITY_TYPE_NAME)
        description = request.form.get(K_ENTITY_TYPE_DESCRIPTION)

        if entity_type_name is not None \
                and model.EntityType.query.filter_by(entity_type_name=entity_type_name).first() is not None:
            return {'message': 'Entity type with name %s already exists' % entity_type_name}
        else:
            entity_type = model.EntityType(entity_type_name=entity_type_name, description=description)
            db.session.add(entity_type)
            db.session.commit()
            return {'message': 'Entity type creation succeed!'}

    def delete(self):
        entity_type = model.EntityType.query.filter_by(id=request.form.get(K_ENTITY_TYPE_ID)).first()

        db.session.delete(entity_type)
        db.session.commit()

        return {'message': 'Entity type deletion succeed!'}

    def post(self):
        entity_type_id = request.form.get(K_ENTITY_TYPE_ID)
        entity_type_name = request.form.get(K_ENTITY_TYPE_NAME)
        description = request.form.get(K_ENTITY_TYPE_DESCRIPTION)

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


K_ENTITY_ID = 'entity_id'
K_ENTITY_NAME = 'entity_name'
K_ENTITY_ENTITY_TYPE_NAME = 'entity_type_name'
K_ENTITY_ENTITY_TYPE_ID = 'entity_type_id'
K_ENTITY_DESCRIPTION = 'description'
entity_fields = {
    K_ENTITY_ID: fields.Integer(attribute='id'),
    K_ENTITY_NAME: fields.String(attribute='entity_name'),
    K_ENTITY_ENTITY_TYPE_NAME: fields.String(attribute='entity_type.entity_type_name'),
    K_ENTITY_ENTITY_TYPE_ID: fields.Integer(attribute='entity_type_id'),
    K_ENTITY_DESCRIPTION: fields.String(attribute='description')
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
            entity_id = request.args[K_ENTITY_ID]
        except BaseException:
            entity_id = None
        try:
            entity_type_id = request.args[K_ENTITY_ENTITY_TYPE_ID]
        except BaseException:
            entity_type_id = None
        try:
            description = request.args[K_ENTITY_DESCRIPTION]
        except BaseException:
            description = None
        try:
            entity_name = request.args[K_ENTITY_NAME]
        except BaseException:
            entity_name = None

        results = model.Entity.query.filter(
            model.Entity.id == entity_id if entity_id is not None else text(''),
            model.Entity.entity_type_id == entity_type_id if entity_type_id is not None else text(''),
            model.Entity.description == description if description is not None else text(''),
            model.Entity.entity_name == entity_name if entity_name is not None else text('')
        )

        return {'message': '', 'entity_list': results}


K_OPERATION_ID = 'operation_id'
K_OPERATION_NAME = 'operation_name'
K_OPERATION_ENTITY_TYPE_ID = 'entity_type_id'
K_OPERATION_DESCRIPTION = 'description'
operation_fields = {
    K_OPERATION_ID: fields.Integer(attribute='id'),
    K_OPERATION_NAME: fields.String(attribute='operation_name'),
    K_OPERATION_ENTITY_TYPE_ID: fields.Integer(attribute='entity_type_id'),
    K_OPERATION_DESCRIPTION: fields.String(attribute='description')
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
            operation_id = request.args[K_OPERATION_ID]
        except BaseException:
            operation_id = None
        try:
            entity_type_id = request.args[K_OPERATION_ENTITY_TYPE_ID]
        except BaseException:
            entity_type_id = None
        try:
            operation_name = request.args[K_OPERATION_NAME]
        except BaseException:
            operation_name = None
        try:
            description = request.args[K_OPERATION_DESCRIPTION]
        except BaseException:
            description = None

        results = model.Operation.query.filter(
            model.Operation.id == operation_id if operation_id is not None else text(''),
            model.Operation.entity_type_id == entity_type_id if entity_type_id is not None else text(''),
            model.Operation.operation_name == operation_name if operation_name is not None else text(''),
            model.Operation.description == description if description is not None else text('')
        )

        return {'message': '', 'operation_list': results}


K_PRIVILEGE_ID = 'privilege_id'
K_PRIVILEGE_OPERATION_ID = 'operation_id'
K_PRIVILEGE_OPERATION_NAME = 'operation_name'
K_PRIVILEGE_ENTITY_TYPE_NAME = 'entity_type_name'
K_PRIVILEGE_ENTITY_ID = 'entity_id'
K_PRIVILEGE_ENTITY_NAME = 'entity_name'
privilege_fields = {
    K_PRIVILEGE_ID: fields.Integer(attribute='id'),
    K_PRIVILEGE_OPERATION_ID: fields.Integer(attribute='operation_id'),
    K_PRIVILEGE_OPERATION_NAME: fields.String(attribute='operation.operation_name'),
    K_PRIVILEGE_ENTITY_ID: fields.Integer(attribute='entity_id'),
    K_PRIVILEGE_ENTITY_TYPE_NAME: fields.String(attribute='entity.entity_type.entity_type_name'),
    K_PRIVILEGE_ENTITY_NAME: fields.String(attribute='entity.entity_name')

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
            privilege_id = request.args[K_PRIVILEGE_ID]
        except BaseException:
            privilege_id = None
        try:
            operation_id = request.args[K_PRIVILEGE_OPERATION_ID]
        except BaseException:
            operation_id = None
        try:
            entity_id = request.args[K_PRIVILEGE_ENTITY_ID]
        except BaseException:
            entity_id = None

        results = model.Privilege.query.filter(
            model.Privilege.id == privilege_id if privilege_id is not None else text(''),
            model.Privilege.operation_id == operation_id if operation_id is not None else text(''),
            model.Privilege.entity_id == entity_id if entity_id is not None else text('')
        )

        return {'message': '', 'privilege_list': results}


K_GROUP_ID = 'group_id'
K_GROUP_NAME = 'group_name'
K_GROUP_DESCRIPTION = 'description'
group_fields = {
    K_GROUP_ID: fields.Integer(attribute='id'),
    K_GROUP_NAME: fields.String(attribute='group_name'),
    K_GROUP_DESCRIPTION: fields.String(attribute='description')
}
group_list = fields.List(fields.Nested(group_fields))
group_response = {
    'message': fields.String,
    'group_list': group_list
}


K_ROLE_ID = "role_id"
K_ROLE_NAME = "role_name"
K_ROLE_DESCRIPTION = "description"
role_fields = {
    K_ROLE_ID: fields.Integer(attribute='id'),
    K_ROLE_NAME: fields.String(attribute='role_name'),
    K_ROLE_DESCRIPTION: fields.String(attribute='description')
}
role_list = fields.List(fields.Nested(role_fields))
role_response = {
    "message": fields.String,
    "role_list": role_list
}

K_USER_ID = "user_id"
K_USER_NAME = "user_name"
K_USER_EMAIL = "email"
K_USER_PHONE_NUMBER = "phone_number"
K_USER_GROUP_NAME = 'group_name'
K_USER_GENDER = 'gender'
K_USER_PASSWORD = 'password'
user_fields = {
    K_USER_ID: fields.Integer(attribute='id'),
    K_USER_NAME: fields.String(attribute='user_name'),
    K_USER_EMAIL: fields.String(attribute='email'),
    K_USER_PHONE_NUMBER: fields.String(attribute='phone_number'),
    K_USER_GROUP_NAME: fields.String(attribute='group.group_name'),
    K_USER_GENDER: fields.String(attribute='gender')
}
user_list = fields.List(fields.Nested(user_fields))
user_response = {
    "message": fields.String,
    "user_list": user_list
}


class Group(Resource):
    @marshal_with(group_response, envelope='resource')
    def get(self):
        try:
            group_id = request.args[K_GROUP_ID]
        except BaseException:
            group_id = None
        try:
            group_name = request.args[K_GROUP_NAME]
        except BaseException:
            group_name = None
        try:
            description = request.args[K_GROUP_DESCRIPTION]
        except BaseException:
            description = None

        # Access control code here
        # user = check_auth_token(request.form.get('token'))
        # if user is None:
        #     return {'message': 'Invalid token'}
        # if check_access_permission(user, entity_type='group', operation_name='GET'):
        #     results = model.Group.query.filter(
        #         model.Group.id == group_id if group_id is not None else text(''),
        #         model.Group.group_name == group_name if group_name is not None else text(''),
        #         model.Group.description.like("%" + description + "%") if description is not None else text('')
        #     )
        #     message = ''
        # else:
        #     results = None
        #     message = 'You have no permission for this operation'
        results = model.Group.query.filter(
            model.Group.id == group_id if group_id is not None else text(''),
            model.Group.group_name == group_name if group_name is not None else text(''),
            model.Group.description.like("%" + description + "%") if description is not None else text('')
        )
        message = ''

        return {'message': message, 'group_list': results}

    def put(self):
        if request.form.get(K_GROUP_NAME) is None:
            return {'message': 'group_name should not be empty!'}

        if model.Group.query.filter(model.Group.group_name == request.form.get(K_GROUP_NAME)).first() is not None:
            return {'message': 'group_name %s already exists!' % request.form.get(K_GROUP_NAME)}
        group = model.Group(
            group_name=request.form.get(K_GROUP_NAME),
            description=request.form.get(K_GROUP_DESCRIPTION)
        )
        # return 'group_id is %d, group_name is %s, description is %s' % (group.id, group.group_name, group.description)

        db.session.add(group)
        db.session.commit()
        return {'message': 'Group creation succeed!'}

    def delete(self):
        group_id = request.form.get(K_GROUP_ID)

        group_obj = model.Group.query.filter(
            model.Group.id == group_id
        ).first()
        db.session.delete(group_obj)
        db.session.commit()
        return {'message': 'Group deletion succeed!'}

    def post(self):
        group_id = request.form.get(K_GROUP_ID)
        group_name = request.form.get(K_GROUP_NAME)
        description = request.form.get(K_GROUP_DESCRIPTION)

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
        try:
            role_id = request.args[K_ROLE_ID]
        except BaseException:
            role_id = None
        try:
            role_name = request.args[K_ROLE_NAME]
        except BaseException:
            role_name = None
        try:
            description = request.args[K_ROLE_DESCRIPTION]
        except BaseException:
            description = None

        results = model.Role.query.filter(
            model.Role.id == role_id if role_id is not None else text(''),
            model.Role.role_name == role_name if role_name is not None else text(''),
            model.Role.description.like("%" + description + "%") if description is not None else text('')
        )

        return {
            "message": '',
            "role_list": results
        }

    def put(self):
        if request.form.get(K_ROLE_NAME) is None:
            return {"message": "role_name should not be none"}

        role_name = request.form.get(K_ROLE_NAME)
        description = request.form.get(K_ROLE_DESCRIPTION)
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
        role = model.Role.query.filter_by(id=request.form.get(K_ROLE_ID)).first()

        db.session.delete(role)
        db.session.commit()

        return {"message": "Role deletion succeed"}

    def post(self):
        role_id = request.form.get(K_ROLE_ID)
        role_name = request.form.get(K_ROLE_NAME)
        description = request.form.get(K_ROLE_DESCRIPTION)

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
    K_GROUP_ID: fields.Integer,
    K_GROUP_NAME: fields.String,
    K_GROUP_DESCRIPTION: fields.String,
    'role_list': role_list
}
class Group_Roles(Resource):
    @marshal_with(group_roles_response, envelope='resource')
    def get(self):
        try:
            group_id = request.args[K_GROUP_ID]
        except BaseException:
            group_id = None
        try:
            group_name = request.args[K_GROUP_NAME]
        except BaseException:
            group_name = None
        group = model.Group.query.filter(
            model.Group.id == group_id if group_id is not None else text(''),
            model.Group.group_name == group_name if group_name is not None else text('')
        ).first()
        if group is None:
            return {'message': 'No such group'}
        return {
            "message": '',
            "role_list": group.roles,
            K_GROUP_ID: group.id,
            K_GROUP_NAME: group.group_name,
            K_GROUP_DESCRIPTION: group.description
        }

    def post(self):
        group = model.Group.query.filter_by(id=request.form.get(K_GROUP_ID)).first()
        role = model.Role.query.filter_by(id=request.form.get(K_ROLE_ID)).first()
        if role is None or group is None:
            return {'message': 'No such role or group'}

        group.roles.append(role)
        db.session.commit()

        return {'message': ''}
    
    def delete(self):
        group = model.Group.query.filter_by(id=request.form.get(K_GROUP_ID)).first()
        role = model.Role.query.filter_by(id=request.form.get(K_ROLE_ID)).first()
        if role is None or group is None:
            return {'message': 'No such role or group'}

        group.roles.remove(role)
        db.session.commit()


role_groups_response = {
    'message': fields.String,
    K_ROLE_ID: fields.Integer,
    K_ROLE_NAME: fields.String,
    K_ROLE_DESCRIPTION: fields.String,
    'group_list': group_list
}
class Role_Groups(Resource):
    @marshal_with(role_groups_response, envelope='resource')
    def get(self):
        try:
            role_id = request.args[K_ROLE_ID]
        except BaseException:
            role_id = None
        try:
            role_name = request.args[K_ROLE_NAME]
        except BaseException:
            role_name = None

        role = model.Role.query.filter(
            model.Role.id == role_id if role_id is not None else text(''),
            model.Role.role_name == role_name if role_name is not None else text('')
        ).first()

        return {
            "message": '',
            "group_list": role.groups,
            K_ROLE_ID: role.id,
            K_ROLE_NAME: role.role_name,
            K_ROLE_DESCRIPTION: role.description
        }

    def post(self):
        pass


role_privileges_response = {
    'message': fields.String,
    K_ROLE_ID: fields.Integer,
    K_ROLE_NAME: fields.String,
    K_ROLE_DESCRIPTION: fields.String,
    'privilege_list': privilege_list
}
class Role_Privileges(Resource):
    @marshal_with(role_privileges_response, envelope='resource')
    def get(self):
        try:
            role_id = request.args[K_ROLE_ID]
        except BaseException:
            role_id = None
        try:
            role_name = request.args(K_ROLE_NAME)
        except BaseException:
            role_name = None

        role = model.Role.query.filter(
            model.Role.id == role_id if role_id is not None else text(''),
            model.Role.role_name == role_name if role_name is not None else text('')
        ).first()

        if role is not None:
            return {
                'message': '',
                K_ROLE_ID: role.id,
                K_ROLE_NAME: role.role_name,
                K_ROLE_DESCRIPTION: role.description,
                'privilege_list': role.privileges
            }
        else:
            return {
                'message': 'No such role'
            }

    def post(self):
        role = model.Role.query.filter_by(id=request.form.get(K_ROLE_ID)).first()
        privilege = model.Privilege.query.filter_by(id=request.form.get(K_PRIVILEGE_ID)).first()

        if role is None or privilege is None:
            return {'message': 'No such role or privilege!'}

        role.privileges.append(privilege)

        db.session.commit()

        return {'message': ''}

    def delete(self):
        role = model.Role.query.filter_by(id=request.form.get(K_ROLE_ID)).first()
        privilege = model.Privilege.query.filter_by(id=request.form.get(K_PRIVILEGE_ID)).first()

        if role is None or privilege is None:
            return {'message': 'No such role or privilege'}

        role.privileges.remove(privilege)

        db.session.commit()


class User(Resource):
    @marshal_with(user_response, envelope='resource')
    def get(self):
        try:
            user_id = int(request.args[K_USER_ID])
        except BaseException:
            user_id = None
        try:
            user_name = request.args[K_USER_NAME]
        except BaseException:
            user_name = None
        try:
            email = request.args[K_USER_EMAIL]
        except BaseException:
            email = None
        try:
            phone_number = request.args[K_USER_PHONE_NUMBER]
        except BaseException:
            phone_number = None
        try:
            group_name = request.args[K_USER_GROUP_NAME]
        except BaseException:
            group_name = None
        try:
            gender = request.args[K_USER_GENDER]
        except BaseException:
            gender = None

        results = model.User.query.join(model.Group).filter(
            model.User.id == user_id if user_id is not None else text(''),
            model.User.user_name == user_name if user_name is not None else text(''),
            model.User.email == email if email is not None else text(''),
            model.User.phone_number == phone_number if phone_number is not None else text(''),
            model.Group.group_name == group_name if group_name is not None else text(''),
            model.User.gender == gender if gender is not None else text('')
        )

        return {
            "message": '',
            "user_list": results
        }

    def put(self):
        if request.form.get(K_USER_NAME) is None or request.form.get(K_USER_PASSWORD) is None:
            return {"message": "user_name or password should not be empty user_name is: %s"
                    % request.form.get('user_name')}

        user_name = request.form.get(K_USER_NAME)
        if model.User.query.filter_by(user_name=user_name).first() is not None:
            return {"message": "User with name is already exists" % user_name}

        user = model.User(
            user_name=user_name,
            email=request.form.get(K_USER_EMAIL),
            password=request.form.get(K_USER_PASSWORD),
            phone_number=request.form.get(K_USER_PHONE_NUMBER),
            group=model.Group.query.filter_by(group_name=request.form.get(K_USER_GROUP_NAME)).first(),
            gender=request.form.get(K_USER_GENDER)
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User creation succeed"}

    def delete(self):
        user = model.User.query.filter_by(id=request.form.get(K_USER_ID)).first()
        if user is None:
            return {"message": "No user with id %d" % request.form.get(K_USER_ID)}

        db.session.delete(user)
        db.session.commit()

    def post(self):
        user_id = request.form.get(K_USER_ID)
        user_name = request.form.get(K_USER_NAME)
        email = request.form.get(K_USER_EMAIL)
        phone_number = request.form.get(K_USER_PHONE_NUMBER)
        group = model.Group.query.filter_by(group_name=request.form.get(K_USER_GROUP_NAME)).first()
        gender = request.form.get(K_USER_GENDER)

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
