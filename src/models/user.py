from src.app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """Model for user accounts."""

    # __tablename__ = 'user'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=False,
                      nullable=False)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)