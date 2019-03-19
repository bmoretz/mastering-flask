import datetime

from webapp import db

tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column('username', db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))

    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, username=""):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True }

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default = datetime.datetime.now)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )

    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title=""):
        self.title = title

    def __repr__(self):
        return "<Post '{}'>".format(self.title)

class Comment(db.Model):
    __tablename__ = 'comment'
    __table_args__ = {'extend_existing': True}     
    
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default = datetime.datetime.now)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])

class Tag(db.Model):
    __tablename__ = 'tag'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, title=""):
        self.title = title

    def __repr__(self): 
        return "<Tag '{}'>".format(self.title)

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()