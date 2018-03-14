#coding=utf-8
import os
from flask import Flask
from config import config
from flask_restful import Resource, Api
from flask_mongoengine  import MongoEngine
from pymongo import MongoClient

env = os.getenv('FALSK_CONFIG') or 'default'

URI = 'mongodb://%s:%d' % (config[env].MONGO_HOST, config[env].MONGO_PORT)

client = MongoClient(URI)

pydb = client[config[env].MONGO_DBNAME]

api = Api()
db = MongoEngine()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    api.init_app(app)
    db.init_app(app)

    #蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app