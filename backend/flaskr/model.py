'''
@Author: your name
@Date: 2020-04-23 15:16:31
@LastEditTime: 2020-04-26 16:53:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/model.py
'''
from ext import db


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

    # 指向用户组的关系
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

    def __repr__(self):
        return '<RolePrivilege %r>' % self.id


class Privilege(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=True)

    def __repr__(self):
        return '<Privilege %r>' % self.id


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.id'), nullable=False)
    operation_name = db.Column(db.String(80), unique=True, nullable=False)
    # restful_api = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return '<Operation %r>' % self.operation_name


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.id'), nullable=False)
    entity_name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    entity_info_id = db.Column(db.Integer, nullable=False, unique=False)

    entity_type = db.relationship('EntityType', backref=db.backref('entities', lazy=True))

    def __repr__(self):
        return '<Resource %r>' % self.res_name

class EntityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    res_type_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return '<ResType %r>' % self.res_type_name
