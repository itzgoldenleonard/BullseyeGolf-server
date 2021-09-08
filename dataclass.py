"""Test of dataclass for the database."""

from dataclasses import dataclass, field
import json
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass()
class DB:
    """The database class."""

    db_id: str = ""
    hole: int = 0
    img: str = "None"
    show_title: bool = True
    date: str = "1970-01-01"
    scores: list['Score'] = field(default_factory=list)

    def write(self):
        """Write the database object to file."""
        with open('DB/' + self.db_id + '.json', 'w') as file:
            json.dump(self.to_dict(), file)

    def serialize(self):
        """Return a json serialized version of the DB object for the API."""
        return json.dumps(self.to_dict())

    def add_score(self, name, score):
        """Add a new score to the database."""
        self.scores.append(Score(name, score))


def read(db_id: str) -> DB:
    """Return a DB object from a data file."""
    with open('DB/' + db_id + '.json', 'r') as file:
        return DB.from_dict(json.loads(file.read()))


@dataclass(frozen=True)  # TODO: I need to figure out how to reconstruct this properly from json
class Score:
    """Class for the individual scores."""

    name: str
    score: float
