
import uuid

from app import db
from sqlalchemy.dialects.postgresql import UUID

from .playlist import Playlist


class SongInPlaylist(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    playlist_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('playlist.uuid'), nullable=False)
    spotify_song_id = db.Column(db.String(120), unique=True, nullable=False)

    playlist = db.relationship('Playlist', backref=db.backref('songs', lazy=True))

    def __repr__(self):
        return '<Song in playlist %r>' % self.spotify_song_id
