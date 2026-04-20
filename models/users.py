import uuid
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID
from db import db


class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    active = db.Column(db.Boolean, nullable=False, default=True)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ["user_id", "first_name", "last_name", "email", "active"]

    user_id = ma.fields.UUID()
    first_name = ma.fields.String()
    last_name = ma.fields.String()
    email = ma.fields.String(required=True)
    active = ma.fields.Boolean(required=True)


Users.schema = UsersSchema()
