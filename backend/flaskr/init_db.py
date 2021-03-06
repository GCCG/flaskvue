'''
@Author: your name
@Date: 2020-04-29 09:08:40
@LastEditTime: 2020-05-14 16:47:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/init_db.py
'''
from .app import create_app
from .ext import db
from .model import Group, User, Role, Privilege, EntityType, Operation, Entity

def create_entity_types(db):
    entity_type = EntityType(entity_type_name='entity_type', description='Entity types that the platform owns')
    entity = EntityType(entity_type_name='entity', description='Entities that the platform owns')
    user = EntityType(entity_type_name='user', description='Visitors that can operate this platform')
    role = EntityType(entity_type_name='role', description='Role is a collection of privileges')
    group = EntityType(entity_type_name='group', description='Group is a collection of roles')
    privilege = EntityType(entity_type_name='privilege', description='Privilege for platform operation')
    operation = EntityType(entity_type_name='operation', description='Platform operations')

    db.session.add(entity_type)
    db.session.add(entity)
    db.session.add(user)
    db.session.add(role)
    db.session.add(group)
    db.session.add(privilege)
    db.session.add(operation)
    db.session.commit()

    print("EntityType created!")

def create_operations(db):
    group_entity_type = EntityType.query.filter_by(entity_type_name='group').first()
    group_create = Operation(operation_name='PUT')
    group_read = Operation(operation_name='GET')
    group_update = Operation(operation_name='POST')
    group_delete = Operation(operation_name='DELETE')

    group_entity_type.operations.append(group_create)
    group_entity_type.operations.append(group_read)
    group_entity_type.operations.append(group_update)
    group_entity_type.operations.append(group_delete)

    db.session.commit()

    print("Operation created!")

def create_entity(db):
    entity = Entity(entity_name='ALL', description='This entity represents all entities which belong to one entity type,\
                                                    if one privilege relates to this entity, that means \
                                                    the operation which relates to this privilege can act on \
                                                    any entity belongs to the entity type to which the operation \
                                                    belongs.', entity_info_id=0)
    entity_type = EntityType.query.filter_by(entity_type_name='group').first()
    entity_type.entities.append(entity)

    db.session.commit()

    print("Entity created!")


def create_privileges(db):
    # Get entity that represents all entities in one type
    entity_all = Entity.query.filter_by(entity_name='ALL').first()

    create_p = Privilege(entity=entity_all, operation=Operation.query.filter_by(operation_name='PUT').first())
    db.session.add(create_p)

    read_p = Privilege(entity=entity_all, operation=Operation.query.filter_by(operation_name='GET').first())
    db.session.add(read_p)

    update_p = Privilege(entity=entity_all, operation=Operation.query.filter_by(operation_name='POST').first())
    db.session.add(update_p)

    delete_p = Privilege()
    delete_p.operation = Operation.query.filter_by(operation_name='DELETE').first()
    delete_p.entity = entity_all
    db.session.add(delete_p)

    db.session.commit()

    print("Privilege created!")


def create_groups(db):
    admin_group = Group(group_name='admin_group', description='Contains superusers of this platform')
    normal_group = Group(
        group_name='normal_group',
        description="Contains users that can only execute some restricted actions")
    db.session.add(admin_group)
    db.session.add(normal_group)
    db.session.commit()

    print('Groups created!')

def create_users(db):
    admin_group = Group.query.filter_by(group_name='admin_group').first()
    admin = User(user_name='admin', password='admin', email='1106018500@qq.com', group=admin_group)

    normal_group = Group.query.filter_by(group_name='normal_group').first()
    chicken = User(user_name='chicken', password='123456', email='110@qq.com', group=normal_group)

    admin_group.users.append(admin)
    normal_group.users.append(chicken)
    db.session.commit()

    print('Users created!')

def create_roles(db):
    group_namager = Role(role_name='group_manager', description='The manager of groups of this platform')
    print("role name is: %s" % group_namager.role_name)
    entity_all = Entity.query.filter_by(entity_name='ALL').first()
    group_operations = EntityType.query.filter_by(entity_type_name='group').first().operations
    for operation in group_operations:
        group_namager.privileges.append(
            Privilege.query.filter_by(operation_id=operation.id, entity_id=entity_all.id).first())

    db.session.add(group_namager)
    db.session.commit()

    print("Roles created!")

def config_privileges(db):
    admin_group = Group.query.filter_by(group_name='admin_group').first()
    role = Role.query.filter_by(role_name='group_manager').first()
    print("role name is: %s" % role.role_name)
    admin_group.roles.append(Role.query.filter_by(role_name='group_manager').first())

    db.session.commit()

    print("Privilege configured!")


app = create_app()
with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()

    create_entity_types(db)
    create_operations(db)
    create_entity(db)
    create_privileges(db)
    create_groups(db)
    create_users(db)
    create_roles(db)
    config_privileges(db)
