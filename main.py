from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
 
app = Flask(__name__) 
app.config.from_object(DevConfig) 
db = SQLAlchemy(app)

@app.route('/') 
def home(): 
    return '<h1>Hello World!</h1>' 
 
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column('user_name', db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)

if __name__ == '__main__': 
    app.run(host='0.0.0.0')