__author__ = 'Velu'
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask.ext.moment import Moment

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x97z\xe7\xdf\xbd\xbc\xc2O&y\xf9&><\x1a\x8a\xbd\xad\x12R>m\x17\x01'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bookmarks.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

# configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

#for display timestamps
moment = Moment(app)

#from forms import BookmarkForm
import models
import views

#python manage.py db init
#python manage.py db migrate -m "initial"
#python manage.py db upgrade
#python manage.py db migrate -m "tags"
#python manage.py db upgrade
