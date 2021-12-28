from flask import Response, request
from flask_restful import Resource
from .dataclass import read, write, Tournament, Hole


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
        tournament: str = Tournament.deserialize(read(f'/bullseyegolf/DB/{db_id}.json'))
        for element in tournament.holes:
            if element == hole_number:
                return Response(element.serialize(), mimetype="application/json", status=200)

        return Response("Hole not found", status=404)

    # def post(self, db_id: str, hole_number: int):

