from flask import request, jsonify

from db import db, cache
from models.users import Users


def add_user():
    post_data = request.get_json()

    user = Users(**post_data)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "user created", "results": {"user_id": user.user_id, "first_name": user.first_name}}), 201


def get_all_users():
    users = db.session.query(Users).all()

    return jsonify({"message": "users found", "results": Users.schema.dump(users, many=True)}), 200


def get_by_user_id(user_id):
    cache_key = f"user:{user_id}"

    if cache.has(cache_key):
        user = cache.get(cache_key)
    else:
        user = db.session.query(Users).filter(Users.user_id == user_id).first()
        cache.set(cache_key, user, timeout=20)

    if not user:
        return jsonify({"message": "user not found"}), 404

    return jsonify({"message": "user found", "results": Users.schema.dump(user)}), 200


def update_user(user_id):
    post_data = request.get_json()

    user = db.session.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        return jsonify({"message": "user not found"}), 404

    for field in ["first_name", "last_name", "email", "active"]:
        if field in post_data:
            setattr(user, field, post_data[field])

    db.session.commit()

    return jsonify({"message": "user updated", "results": Users.schema.dump(user)}), 200


def delete_user(user_id):
    user = db.session.query(Users).filter(Users.user_id == user_id).first()
    if not user:
        return jsonify({"message": "user not foun"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "user deleted"}), 200
