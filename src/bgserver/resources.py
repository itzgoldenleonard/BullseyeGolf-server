import os
import json
from flask import Response, request
from flask_restful import Resource
from .dataclass import read, write, Tournament, Hole, Score, ShortTournament


class Admin(Resource):
    def post(self, db_id: str):
        tournament: str = Tournament.deserialize(request.get_data(as_text=True))
        write(tournament.serialize(), f'/bullseyegolf/DB/{db_id}.json')
        return Response("OK", status=200)


class UserTournament(Resource):
    def get(self, db_id: str):
        return Response(read(f'/bullseyegolf/DB/{db_id}.json'), mimetype="application/json", status=200)


class UserHole(Resource):
    def get(self, db_id: str, hole_number: int):
        tournament = Tournament.deserialize(read(f'/bullseyegolf/DB/{db_id}.json'))
        for element in tournament.holes:
            if element == hole_number:
                return Response(element.serialize(), mimetype="application/json", status=200)

        return Response("Hole not found", status=404)

    def post(self, db_id: str, hole_number: int):
        score = Score.deserialize(request.get_data(as_text=True))
        tournament = Tournament.deserialize(read(f'/bullseyegolf/DB/{db_id}.json'))
        for element in tournament.holes:
            if element == hole_number:
                element.scores.append(score)
                write(tournament.serialize(), f'/bullseyegolf/DB/{db_id}.json')
                return Response("OK", status=200)

        return Response("Holey not found", status=404)

class TournamentList(Resource):
    def get(self):
        tournament_list: list = []
        for i in os.listdir('/bullseyegolf/DB'):
            tournament_list.append(ShortTournament.generate(i).to_dict())

        return Response(json.dumps(tournament_list), mimetype="application/json", status=200)
