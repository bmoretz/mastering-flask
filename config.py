from urllib.parse import urlparse, quote_plus

class Config(object):
    POSTS_PER_PAGE = 10

class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = b'K\xa7G\xa5q\x80\x97\xd1&\x94V\xea\x91J\x98\xb8c\x1b\xdc`\xf5?\xb1\x16'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = b'\xcf7\xa6\x91\xf8\x1be\xb8\x0b~\xe5\xf9\x17\xa1\x97\x8b_\x07\x7fcLb\xc4t'