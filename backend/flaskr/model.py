'''
@Author: your name
@Date: 2020-04-23 15:16:31
@LastEditTime: 2020-04-29 16:02:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/model.py
'''
from ext import db
from flask import jsonify


# 应用的模型设计，依照文件“平台数据模型”
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

    def jsonify(self):
        return jsonify(
            user_id=self.id,
            user_name=self.user_name,
            email=self.email,
            phone_number=self.phone_number,
            group_id=self.group_id,
            gender=self.gender)


group_role = db.Table(
    'group_role',
    db.Column('group_id', db.Integer, db.ForeignKey('group.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)

    roles = db.relationship(
        'Role',
        secondary=group_role,
        lazy='subquery',
        backref=db.backref('groups', lazy=True)
    )

    def __repr__(self):
        return '<Group %r>' % self.group_name

    def jsonify(self):
        return jsonify(
            group_id=self.id,
            group_name=self.group_name,
            description=self.description
        )


role_privilege = db.Table(
    'role_privilege',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('privilege_id', db.Integer, db.ForeignKey('privilege.id'), primary_key=True)
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)

    privileges = db.relationship(
        'Privilege',
        secondary=role_privilege,
        lazy='subquery',
        backref=db.backref('roles', lazy=True)
    )

    def __repr__(self):
        return '<Role %r>' % self.role_name

    def jsonify(self):
        return jsonify(
            role_id=self.id,
            role_name=self.role_name,
            description=self.description
        )


class Privilege(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # privilege_name = db.Column(db.String(80), nullable=False, unique=True)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.id'), nullable=True)

    operation = db.relationship('Operation', backref=db.backref('privileges', lazy=True))
    entity = db.relationship('Entity', backref=db.backref('privileges', lazy=True))

    def __repr__(self):
        return '<Privilege %r>' % self.id

    def jsonify(self):
        return jsonify(
            privilege_id=self.id,
            operation_id=self.operation_id,
            entity_id=self.entity_id
        )


class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.id'), nullable=False)
    operation_name = db.Column(db.String(80), unique=True, nullable=False)
    # restful_api = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    entity_type = db.relationship('EntityType', backref=db.backref('operations', lazy=True))

    def __repr__(self):
        return '<Operation %r>' % self.operation_name

    def jsonify(self):
        return jsonify(
            operation_id=self.id,
            entity_type_id=self.entity_type_id,
            operation_name=self.operation_name,
            description=self.description
        )


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_type_id = db.Column(db.Integer, db.ForeignKey('entity_type.id'), nullable=False)
    entity_name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    entity_info_id = db.Column(db.Integer, nullable=False, unique=False)

    entity_type = db.relationship('EntityType', backref=db.backref('entities', lazy=True))

    def __repr__(self):
        return '<Resource %r>' % self.res_name

    def jsonify(self):
        return jsonify(
            entity_id=self.id,
            entity_type_id=self.entity_type_id,
            entity_name=self.entity_name,
            entity_info_id=self.entity_info_id,
        )

class EntityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity_type_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return '<ResType %r>' % self.entity_type_name

    def jsonify(self):
        return jsonify(
            entity_type_id=self.id,
            entity_type_name=self.entity_type_name,
            description=self.description
        )


class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(80), unique=True, nullable=False)
    station_url = db.Column(db.String(200), unique=False, nullable=True)
    login_rc = db.Column(db.Text, unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)
    station_type_id = db.Column(db.Integer, db.ForeignKey('station_type.id'), nullable=False)

    def __repr__(self):
        return '<Station %r>' % self.station_name

    def jsonify(self):
        return jsonify(
            station_id=self.id,
            station_name=self.station_name,
            station_url=self.station_url,
            login_rc=self.login_rc,
            description=self.description,
            station_type_id=self.station_type_id
        )

class StationType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_type_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=False)


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_d = db.Column(db.Integer, db.ForeignKey('station.id'), nullable=False)
    device_name = db.Column(db.String(80), unique=False, nullable=False)
    ip_address = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return '<Device %r>' % self.device_name

    def jsonify(self):
        return jsonify(
            device_id=self.id,
            station_id=self.station_id,
            device_name=self.device_name,
            ip_address=self.ip_address,
            description=self.description
        )


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)
    port = db.Column(db.String(20), unique=False, nullable=False)
    apis = db.Column(db.Text, unique=False, nullable=True)
    ip_address = db.Column(db.String(80), unique=False, nullable=False)
    service_name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<Service %r>' % self.service_name

    def jsonify(self):
        return jsonify(
            service_id=self.id,
            service_name=self.service_name,
            device_id=self.device_id,
            service_type_id=self.service_type_id,
            port=self.port,
            apis=self.apis,
            ip_address=self.ip_address,
            description=self.description
        )


class ServiceType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_type_name = db.Column(db.String(80), unique=True, nullable=False)
    apis = db.Column(db.Text, unique=False, nullable=False)
    description = db.Column(db.Text, unique=False, nullable=True)

    def __repr__(self):
        return '<ServiceType %r>' % self.service_type_name

    def jsonify(self):
        return jsonify(
            service_type_id=self.id,
            service_type_name=self.service_type_name,
            apis=self.apis,
            description=self.description
        )
