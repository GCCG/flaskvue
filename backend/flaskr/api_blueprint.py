'''
@Author: your name
@Date: 2020-05-09 08:40:53
@LastEditTime: 2020-05-15 12:01:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/api_blueprint.py
'''
from .resources.auth import Login, Register
from .resources.auth_mng import Group, Role, User, Group_Roles, Role_Groups
from .resources.auth_mng import EntityType, Entity, Operation, Privilege, Role_Privileges
from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)
api.add_resource(Login, '/auth/login')
api.add_resource(Register, '/auth/register')
api.add_resource(Group, '/group')
api.add_resource(Role, '/role')
api.add_resource(User, '/user')
api.add_resource(Group_Roles, '/group_roles')
api.add_resource(Role_Groups, '/role_groups')
api.add_resource(Role_Privileges, '/role_privileges')
api.add_resource(EntityType, '/entity_type')
api.add_resource(Entity, '/entity')
api.add_resource(Operation, '/operation')
api.add_resource(Privilege, '/privilege')
