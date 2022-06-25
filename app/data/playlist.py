
import uuid

from app import db
from sqlalchemy.dialects.postgresql import UUID


class Playlist(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spotify_playlist_id = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Playlist %r>' % self.spotify_playlist_id
