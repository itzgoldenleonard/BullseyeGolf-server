from flask import Response, request
from flask_restful import Resource
from .dataclass import read, write, Tournament


class OnlineTest(Resource):
    def get(self):
        return Response("Hello World! Now with flask-restful", status=200)


class Admin(Resource):
    def post(self, db_id):
        tournament: str = Tournament.deserialize(request.get_data(as_text=True))
        write(tournament.serialize(), f'/bullseyegolf/DB/{db_id}.json')
        return Response("OK", status=200)

class UserTournament(Resource):
    def get(self, db_id):
        return Response(read(f'/bullseyegolf/DB/{db_id}.json'), mimetype="application/json", status=200)
