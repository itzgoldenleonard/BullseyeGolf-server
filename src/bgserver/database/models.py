from .db import db

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    key = db.StringField(required=True)

class Score(db.EmbeddedDocument):
    player_name = db.StringField(required=True)
    player_score = db.FloatField(required=True)


class Hole(db.EmbeddedDocument):
    hole_number = db.IntField(required=True)
    hole_text = db.StringField(required=True)
    hole_image = db.StringField(required=True)
    hole_sponsor = db.StringField(required=True)
    game_mode = db.StringField()
    scores = db.ListField(db.EmbeddedDocumentField(Score))

class Tournament(db.Document):
    tournament_id = db.StringField(required=True, unique=True) # primary_key=True
    tournament_name = db.StringField(required=True)
    t_start = db.IntField(required=True)
    t_end = db.IntField(required=True)
    tournament_image = db.StringField(required=True)
    tournament_sponsor = db.StringField(required=True)
    holes = db.ListField(db.EmbeddedDocumentField(Hole))
    owner = db.ReferenceField(User) # Has to be stripped out before sending to client
