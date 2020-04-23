'''
@Author: your name
@Date: 2020-04-21 11:01:42
@LastEditTime: 2020-04-23 15:24:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/__init__.py
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# 应用的模型设计，依照文件“平台ER图”
# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone_number = db.Column(db.String(120), unique=True, nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    gender = db.Column(db.String(1), unique=False, nullable=True)

    group = db.relationship('Group', backref=db.backref('users', lazy=True))

    def __repr__(self):
        return '<User %r>' % self.user_name


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return '<Group %r>' % self.group_name


class GroupRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __repr__(self):
        return '<GroupRole %r>' % self.id


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.role_name


class RolePrivilege(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    privilege_id = db.Column(db.Integer, db.ForeignKey('privilege.id'), nullable=False)


class Privilege(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=True)


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=True)
    operation_name = db.Column(db.String(80), unique=True, nullable=False)
    restful_api = db.Column(db.String(80), unique=True, nullable=False)


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    res_type_id = db.Column(db.Integer, db.ForeignKey('res_type.id'), nullable=False)
    res_name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)


class ResType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    res_type_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

#
