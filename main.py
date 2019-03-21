import random
import os
from config import DevConfig
from webapp import create_app, db
from flask_migrate import Migrate, upgrade

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())
migrate = Migrate(app, db)

from flask import render_template, session, g
from flask.views import View

from webapp.blog.models import Post, Comment
from webapp.auth.models import User

class GenericListView(View):

    def __init__(self, model, list_template='generic_list.html'):
        self.model = model
        self.list_template = list_template
        self.columns = self.model.__mapper__.columns.keys()
        # Call super python3 style
        super(GenericListView, self).__init__()

    def render_template(self, context):
        return render_template(self.list_template, **context)

    def get_objects(self):
        return self.model.query.all()

    def dispatch_request(self):
        context = {'objects':self.get_objects(),
                    'columns':self.columns}
        return self.render_template(context)

app.add_url_rule(
    '/generic_posts', view_func=GenericListView.as_view(
        'generic_posts', model=Post)
    )

app.add_url_rule(
    '/generic_users', view_func=GenericListView.as_view(
        'generic_users', model=User)
)

app.add_url_rule(
    '/generic_comments', view_func=GenericListView.as_view(
        'generic_comments', model=Comment)
)

@app.before_request
def before_request():
    session['page_loads'] = session.get('page_loads', 0) + 1
    g.random_key = random.randrange(1, 10)

if __name__ == '__main__':
    app.run(host='0.0.0.0')