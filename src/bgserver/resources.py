from flask import Response, request, jsonify
from flask_restful import Resource
import time
from .database.models import Tournament, User, ShortTournament

class TournamentResource(Resource):
    def get(self, username: str, tournament_id: str):
        tournament = Tournament.objects(tournament_id=tournament_id).exclude('owner', 'id').first().to_json()
        return Response(tournament, mimetype="application/json", status=200)

    def post(self, username: str, tournament_id: str): # This implementation is only for testing the user API, it's not proper
        data = request.get_json()
        tournament = Tournament(**data)
        tournament.owner = User.objects(username=username).first()
        tournament.save()
        id = tournament.id
        return Response(str(id), status=200)


class TournamentListResource(Resource):
    def get(self, username: str):
        tournaments = Tournament.objects(owner=User.objects(username=username).first()).exclude('tournament_image', 'holes')
        short_tournaments = [ShortTournament.from_tournament(e) for e in tournaments]
        return jsonify(short_tournaments)
