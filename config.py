class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://bmoretz:l3tm31n@DATACENTER:1433/FLASK?driver=ODBC+Driver+13+for+SQL+Server"
    SQLALCHEMY_ECHO = True