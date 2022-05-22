from .db import db
from dataclasses import dataclass
import mongoengine
import time

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    key = db.StringField(required=True)

class Score(db.EmbeddedDocument):
    player_name = db.StringField(required=True)
    player_score = db.FloatField(required=True)

class Hole(db.EmbeddedDocument):
    hole_number = db.IntField(required=True)
    hole_text = db.StringField(required=True, default="")
    hole_image = db.StringField(required=True, default="")
    hole_sponsor = db.StringField(required=True, default="")
    game_mode = db.StringField(default="")
    scores = db.SortedListField(db.EmbeddedDocumentField(Score), ordering="player_score")

class Tournament(db.Document):
    tournament_id = db.StringField(required=True, unique=True) # primary_key=True
    tournament_name = db.StringField(required=True)
    t_start = db.IntField(required=True, default=time.time())
    t_end = db.IntField(required=True, default=time.time() + 86400)
    tournament_image = db.StringField(required=True, default="")
    tournament_sponsor = db.StringField(required=True, default="")
    holes = db.SortedListField(db.EmbeddedDocumentField(Hole), ordering="hole_number")
    owner = db.ReferenceField(User, reverse_delete_rule=mongoengine.CASCADE) # Has to be stripped out before sending to client

@dataclass(frozen=True)
class ShortTournament():
    tournament_id: str = ""
    tournament_name: str = ""
    t_start: int = 0
    t_end: int = 0
    active: bool = False

    def from_tournament(tournament: Tournament) -> "ShortTournament":
        active = True if tournament.t_start < int(time.time()) < tournament.t_end else False
        return ShortTournament(tournament.tournament_id, tournament.tournament_name, tournament.t_start, tournament.t_end, active)

