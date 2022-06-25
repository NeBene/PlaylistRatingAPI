
import uuid

from app import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email, *args, **kwargs):
        super().__init__(email=email, *args, **kwargs)

    def __repr__(self):
        return '<User %r>' % self.email
