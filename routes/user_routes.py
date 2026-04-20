from flask import Blueprint
from controllers import users_controller

from db import cache

user_routes = Blueprint("user", __name__)


@user_routes.route("/user", methods=["POST"])
def add_user():
    return users_controller.add_user()


@user_routes.route("/users", methods=["GET"])
@cache.cached(timeout=20)
def get_all_users():
    return users_controller.get_all_users()


@user_routes.route("/user/<user_id>", methods=["PUT"])
def update_user(user_id):
    return users_controller.update_user(user_id)


@user_routes.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return users_controller.delete_user(user_id)
