"""This file contains all the logic for database handling"""
import json
from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

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

@dataclass_json()
@dataclass(frozen=True)
class Tournament:
    """Class for storing individual tournaments"""
    
    tournament_name: str = "",
    t_start: int = 1,
    t_end: int = 2,
    tournament_image: str = "",
    tournament_sponsor: str = "",
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

    def serialize(self) -> str:
        """Return a json serialized version of the object"""
        return json.dumps(self.to_dict())

    def deserialize(string: str):
        """Construct a Hole object from a json string"""
        return ShortTournament.from_dict(json.loads(string))



def write(string: str, filename: str):
    """Write a string to a file"""
    with open(filename, 'w') as file:
        file.write(string)

def read(filename: str) -> str:
    """Read a file and return its contents as a string"""
    with open(filename, 'r') as file:
        return file.read()

