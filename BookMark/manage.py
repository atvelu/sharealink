__author__ = 'Velu'

from bookmark import app, db
from bookmark.models import User, Bookmark, Tag
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

#from bookmark.bookmark import db
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
    #db.create_all()
    reindert = User(username="velu", email="velu@example.com", password="test")
    db.session.add(reindert)

    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=reindert, tags=tags))

    for name in ["python", "flask", "webdev", "programming", "news", "orm", "database","fun","coolstuff"]:
        db.session.add(Tag(name=name))
    db.session.commit()

    add_bookmark("http://www.python.org", "python - my fav language", "python,programming,flask")
    add_bookmark("http://www.flask.pocoo.org","Flask: web development", "python,flask,webdev")
    add_bookmark("http://www.reddit.com","Reddit", "news, fun")
    add_bookmark("http://www.sqlalmeyo.org","ORM framework", "python,orm,database")
    add_bookmark("http://www.initializr.com","HTML 5", "webdev")
    add_bookmark("http://www.stackoverflow.com", "Q&A", "programming")
    add_bookmark("http://www.djangoproject.org","Django", "python,webdev")
    add_bookmark("http://www.Ipython.org","Ipython", "python")

    arjen = User(username="user1", email="user1@example.com", password="test")
    db.session.add(arjen)
    db.session.commit()
    print 'Initialized the database'

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data?"):
        db.drop_all()
        print "Dropped the database"


if __name__ == '__main__':
    manager.run()