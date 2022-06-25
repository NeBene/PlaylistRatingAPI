
import uuid

from app import db
from sqlalchemy.dialects.postgresql import UUID

from .song_in_playlist import SongInPlaylist
from .user import User


class UserSongRating(db.Model):
    uuid = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    song_in_playlist_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('song_in_playlist.uuid'), nullable=False)
    user_uuid = db.Column(UUID(as_uuid=True), db.ForeignKey('user.uuid'), nullable=False)
    spotify_song_id = db.Column(db.String(120), unique=True, nullable=False)
    liked = db.Column(db.Boolean(), nullable=False)

    song_in_playlist = db.relationship('SongInPlaylist', backref=db.backref('song_ratings', lazy=True))
    user = db.relationship('User', backref=db.backref('user_ratings', lazy=True))

    def __repr__(self):
        return '<Rating %r>' % self.uuid
