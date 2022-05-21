from flask import Response, request, jsonify
from flask_restful import Resource
import time
from .database.models import Tournament, User, ShortTournament, Score

class TournamentResource(Resource):
    def get(self, username: str, tournament_id: str):
        tournament = Tournament.objects(tournament_id=tournament_id).exclude('owner', 'id').first().to_json()
        return Response(tournament, mimetype="application/json", status=200)

    def post(self, username: str, tournament_id: str): # This implementation is only for testing the user API, it's not proper
        data = request.get_json()
        tournament = Tournament(**data)
        tournament.owner = User.objects(username=username).first()
        tournament.save()
        return Response("OK", status=200)


class TournamentListResource(Resource):
    def get(self, username: str):
        tournaments = Tournament.objects(owner=User.objects(username=username).first()).only('tournament_id', 'tournament_name', 't_start', 't_end')
        short_tournaments = [ShortTournament.from_tournament(e) for e in tournaments]
        return jsonify(short_tournaments)


class HoleResource(Resource):
    def get(self, username: str, tournament_id: str, hole_number: int):
        tournament = Tournament.objects(tournament_id=tournament_id).only('holes').first()
        hole = tournament.holes.get(hole_number=hole_number)
        return Response(hole.to_json(), mimetype="application/json", status=200)

    def post(self, username: str, tournament_id: str, hole_number: int):
        data = request.get_json()
        tournament = Tournament.objects(tournament_id=tournament_id).only('holes').first()
        hole = tournament.holes.get(hole_number=hole_number)
        hole.scores.create(**data)
        tournament.update(set__holes=tournament.holes)
        return Response("OK", mimetype="text/plain", status=200)
