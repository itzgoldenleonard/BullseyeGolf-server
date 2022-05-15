from .db import db

class Score(db.Document):
    player_name = db.StringField(required=True)
    player_score = db.FloatField(required=True)
