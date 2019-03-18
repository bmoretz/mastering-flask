from urllib.parse import urlparse, quote_plus

class Config(object):
    POSTS_PER_PAGE = 10

class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://bmoretz:l3tm31n@DATACENTER:1433/FLASK?driver=ODBC+Driver+13+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    params = quote_plus("DRIVER={SQL Server};SERVER=DATACENTER;DATABASE=FLASK;UID=bmoretz;PWD=l3tm31n")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True