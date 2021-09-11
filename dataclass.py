"""Test of dataclass for the database."""
import bisect
from dataclasses import dataclass, field
import json
from dataclasses_json import dataclass_json


@dataclass_json()
@dataclass(frozen=True)
class DB:
    """The database class."""

    db_id: str = ""
    hole: int = 0
    img: str = "None"
    show_title: bool = True
    date: str = "1970-01-01"
    scores: list[dict] = field(default_factory=list)

    def write(self):
        """Write the database object to file."""
        with open('DB/' + self.db_id + '.json', 'w') as file:
            json.dump(self.to_dict(), file)

    def serialize(self):
        """Return a json serialized version of the DB object for the API."""
        return json.dumps(self.to_dict())

    def add_score(self, name: str, score: float) -> int:
        """Add a new score to the database."""

        if not 2 < len(name) < 40:  # check if the name has a valid length
            return -1

        # this is a hacky way of making sure self.scores is always sorted,
        # using a proper dataclass in the list would require me to recreate those objects properly
        # every time I read from the json file
        list_of_scores: list[float] = []
        for i in range(len(self.scores)):
            list_of_scores.append(self.scores[i]['score'])

        bisect.insort_left(list_of_scores, score)  # appends AND sorts the list
        insert_index: int = list_of_scores.index(score)
        self.scores.insert(insert_index, {'name': name, 'score': score})
        return 0


def read(db_id: str) -> DB:
    """Return a DB object from a data file."""
    with open('DB/' + db_id + '.json', 'r') as file:
        return DB.from_dict(json.loads(file.read()))

