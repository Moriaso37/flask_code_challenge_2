from . import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'), nullable=False)

    # Validate rating between 1 and 5
    @staticmethod
    def validate_rating(rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
