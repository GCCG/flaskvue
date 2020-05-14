'''
@Author: your name
@Date: 2020-04-21 11:01:42
@LastEditTime: 2020-05-12 09:13:30
@LastEditors: Please set LastEditors
@Description: 为什么特地要搞这么一个文件只是创建一个app对象呢？因为如果app在__init__.py中的create_app中定义，就无法被
导入到其他文件中使用。比如在manage.py中，需要使用app对象来初始化manager对象以用于
管理数据库。包的__init__.py文件有一些特殊性。
@FilePath: /backend/flaskr/__init__.py
'''
from flask import Flask
# from flaskr import restful_api
# from flaskr.ext import db
from . import ext
# from model import Group
# from flaskr import restful_api
from . import api_blueprint
import os

def create_app(config_file=None):
    # If option instance_relative_config is set true,
    # you should put your file in instance folder
    # which is in root folder of project.
    app = Flask('flaskr', instance_relative_config=True)

    if config_file is None:
        # Load default config file.
        app.config.from_pyfile('config.py')
    else:
        # Load the config file if passed in.
        app.config.from_pyfile(config_file)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initiate database for your app
    ext.db.init_app(app)

    # Initiate APIs for your app
    # restful_api.init_app(app)

    # Register blueprint for restful_api
    app.register_blueprint(api_blueprint.api_bp)

    @app.route('/hello')
    def hello():
        return 'Hello, world!'

    @app.route('/')
    def todo():
        '''
        return {'id': admin.id,
                'group_name': admin.group_name,
                'description': admin.description,
                'Tom': [1, 2, 3, 4, 5]}
        '''
        return 'helloworld'

    return app
