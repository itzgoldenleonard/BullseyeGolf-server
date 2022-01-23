"""This file contains all the logic for database handling"""
import json
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field
import time

@dataclass_json()
@dataclass(frozen=True)
class Score:
    """Class for storing individual scores"""

    player_name: str = ""
    player_score: float = 0.0

    def serialize(self) -> str:
        """Return a json serialized version of the object"""
        return json.dumps(self.to_dict())

    def deserialize(string: str):
        """Construct a Score object from a json string"""
        return Score.from_dict(json.loads(string))

    def __lt__(self, other):
        return self.player_score < other.player_score


@dataclass_json()
@dataclass(frozen=True)
class Hole:
    """Class for storing individual holes"""

    hole_number: int = 0
    hole_text: str = ""
    game_mode: str = ""
    hole_sponsor: str = ""
    hole_image: str = ""
    scores: list[Score] = field(default_factory=list)

    def serialize(self) -> str:
        """Return a json serialized version of the object"""
        return json.dumps(self.to_dict())

    def deserialize(string: str):
        """Construct a Hole object from a json string"""
        return Hole.from_dict(json.loads(string))

    def __eq__(self, other):
        return self.hole_number == other


@dataclass_json()
@dataclass(frozen=True)
class Tournament:
    """Class for storing individual tournaments"""
    
    tournament_name: str = ""
    t_start: int = 1
    t_end: int = 2
    tournament_image: str = ""
    tournament_sponsor: str = ""
    holes: list[Hole] = field(default_factory=list)

    def serialize(self) -> str:
        """Return a json serialized version of the object"""
        return json.dumps(self.to_dict())

    def deserialize(string: str):
        """Construct a Tournament object from a json string"""
        return Tournament.from_dict(json.loads(string))


@dataclass_json()
@dataclass(frozen=True)
class ShortTournament:
    """Class for the list of all tournaments"""

    db_id: str = ""
    tournament_name: str = ""
    active: bool = False
    t_start: int = 0
    t_end: int = 0

    def serialize(self) -> str:
        """Return a json serialized version of the object"""
        return json.dumps(self.to_dict())

    def deserialize(string: str):
        """Construct a ShortTournament object from a json string"""
        return ShortTournament.from_dict(json.loads(string))

    def generate(filename: str):
        """Generate a ShortTournament object from a db file"""
        db_id: str = filename[:len(filename) - 5]
        tournament: Tournament = Tournament.deserialize(read(f'/bullseyegolf/DB/{filename}'))
        tournament_name: str = tournament.tournament_name
        t_start: int = tournament.t_start
        t_end: int = tournament.t_end
        active: bool = True if tournament.t_start < int(time.time()) < tournament.t_end else False
        return ShortTournament(db_id, tournament_name, active, t_start, t_end)



def write(string: str, filename: str):
    """Write a string to a file"""
    with open(filename, 'w') as file:
        file.write(string)

def read(filename: str) -> str:
    """Read a file and return its contents as a string"""
    with open(filename, 'r') as file:
        return file.read()

