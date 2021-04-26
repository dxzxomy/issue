ENV = 'development'
DEBUG = True

import os
import sys
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Sanchuang123#@192.168.56.168:3306/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

class ProductionCondig(Config):
    ENV = 'production'
    DEBUG = False

