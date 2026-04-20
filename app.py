import os
from flask import Flask

from db import db, init_db
from util.blueprints import register_blueprints

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["CACHE_TYPE"] = "RedisCache"
app.config["CACHE_REDIS_URL"] = os.environ.get("REDIS_URL")
app.config["CACHE_DEFAULT_TIMEOUT"] = 10

init_db(app, db)
register_blueprints(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port="8086", debug=True)
