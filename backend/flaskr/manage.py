'''
@Author: your name
@Date: 2020-04-23 21:44:52
@LastEditTime: 2020-04-25 10:14:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /backend/flaskr/manage.py
'''

from app import create_app
from flask_script import Manager, Server
from ext import db
from flask_migrate import Migrate, MigrateCommand
from model import *

app = create_app()
manager = Manager(app=app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)  # Create database mapping commands
manager.add_command('start', Server(port=8000, use_debugger=True))  # Create start comand


if __name__ == '__main__':
    manager.run()