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
        """Construct a Score object from a json string"""
        return Hole.from_dict(json.loads(string))



def write(string: str, filename: str):
    """Write a string to a file"""
    with open(filename, 'w') as file:
        file.write(string)

def read(filename: str) -> str:
    """Read a file and return its contents as a string"""
    with open(filename, 'r') as file:
        return file.read()


"""
# hole = Hole(3, "", "", "sponsor", "", [Score("Jens", 1.15), Score("Peter", 0.36)])
# write(hole.serialize(), "test.json")
hole = Hole(3, "texter", "", "sponsorino", "https://", [Score("Jens", 1.15)])
write(hole.serialize(), "hole.json")
print(f"Original hole object: \n{hole}\n")

file_contents = read("hole.json")
deserialized_hole = Hole.deserialize(file_contents)
print(f"Imposter hole object: \n{deserialized_hole}\n")

print("Tests:")
print(hole.hole_text)
print(deserialized_hole.hole_text)
print("\n")
print(hole.scores[0].player_name)
print(deserialized_hole.scores[0].player_name)
"""
