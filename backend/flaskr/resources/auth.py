'''
@Author: your name
@Date: 2020-04-30 20:59:31
@LastEditTime: 2020-05-18 09:07:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/resources/auth.py
'''

# from flask import Blueprint
from flask_restful import Resource
# from flask_restful import fields, marshal_with
from .. import model
from flask import request, session
from ..ext import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature
from flask import current_app

# Generate auth token.
def generate_auth_token(uid, expiration=7200):
    serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
    token = serializer.dumps({'uid': uid})
    return token.decode('ascii')

# Check if the token is valid.
def check_auth_token(token):
    serializer = Serializer(current_app.config['SECRET_KEY'])
    try:
        s = serializer.loads(token)
    except BadSignature:
        return None

    return model.User.query.filter_by(id=s['uid']).first()

# Check if the user has permission for operating certion entity.
def check_access_permission(user, entity_type, operation_name, entity_id=None):
    group = user.group

    for role in group.roles:
        for privilege in role.privileges:
            if privilege.operation.entity_type.entity_type_name == entity_type \
                    and privilege.operation.operation_name == operation_name \
                    and privilege.entity is not None:
                if privilege.entity.entity_name == 'ALL' or privilege.entity.entity_id == entity_id:
                    return True
    return False


class Auth(Resource):
    def get(self):
        return "Good! You get here!"

class Login(Resource):
    def get(self):
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        user = model.User.query.filter_by(user_name=user_name).first()
        if user_name is None or password is None:
            return {'message': 'User name or password should not be empty'}
        elif user is None:
            return {'message': 'No such user with name %s' % user_name}
        elif user.password != password:
            return {'message': 'Wrong password'}
        else:
            # Extract user privileges and store it in session
            session['user_name'] = user_name
            token = generate_auth_token(user.id)
            return {'message': '', 'token': token}


class Register(Resource):
    def put(self):
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')
        email = request.form.get('email')

        if model.User.query.filter_by(user_name=user_name).first() is not None:
            return {'message': 'User %s already exists' % user_name}
        elif password != password_confirm:
            return {'message': 'Password conflicts with confirmation'}
        elif email is None:
            return {'message': 'Email should not be empty'}
        else:
            user = model.User(user_name=user_name, password=password, email=email)

            db.session.add(user)
            db.session.commit()

            return {'message': ''}


class ForgetPassword(Resource):
    def post(self):
        pass
