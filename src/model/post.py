from ..server import db


class Post(db.Model):
    """Model for posts."""

    __tablename__ = 'posts'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=False,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=False,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    title = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    body = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    tag = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)

    def __repr__(self):
        return '<Post {}>'.format(self.title)