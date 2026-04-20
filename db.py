from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()


def init_db(app, db):
    cache.init_app(app)
    db.init_app(app)
