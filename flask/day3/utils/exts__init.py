from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api
from flask_session import Session

from App.models import db


se = Session()
toolbar = DebugToolbarExtension()
api = Api()


def ext_init(app):
    db.init_app(app=app)
    se.init_app(app=app)
    toolbar.init_app(app=app)
    api.init_app(app=app)
