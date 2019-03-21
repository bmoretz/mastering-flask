import os
from webapp import db, migrate, create_app
from webapp.blog.models import Post, Tag, Comment
from webapp.auth.models import User
from config import DevConfig

app = create_app(DevConfig)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment, Tag=Tag,
                migrate=migrate)