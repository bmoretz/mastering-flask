from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def page_not_found(error):
    return render_template('404.html'), 404
    
def create_app(config_name):

    from .auth import create_module as auth_create_module
    from .blog import create_module as blog_create_module
    from .main import create_module as main_create_module

    app = Flask(__name__)
    app.config.from_object(config_name)

    from webapp.blog.models import db

    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)

    auth_create_module(app)
    blog_create_module(app)
    main_create_module(app)

    app.register_error_handler(404, page_not_found)

    return app