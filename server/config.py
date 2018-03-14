#coding=utf-8

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    UPLOAD_FILE_TYPE = ['patent','cnki','publicnet']
    
    #pymongo
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DBNAME  = 'basedata' 

config = {
    'development': DevelopmentConfig,
    'default':DevelopmentConfig
}