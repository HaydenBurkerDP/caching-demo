import random
import string
from sqlalchemy import insert

from app import app
from db import db
from models.users import Users


def random_string():
    return "".join(random.choices(string.ascii_letters, k=10))


if __name__ == "__main__":
    with app.app_context():
        users = []
        for i in range(10000):
            user = {
                "first_name": random_string(),
                "last_name": random_string(),
                "email": f"{random_string()}@{random_string()}.com",
                "active": random.random() > 0.2
            }

            users.append(user)

        db.session.execute(insert(Users), users)
        db.session.commit()
