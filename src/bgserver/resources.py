from flask import Response, request, jsonify, abort
from flask_restful import Resource
import time
from .database.models import Tournament, User, ShortTournament, Score
from functools import wraps
from mongoengine import DoesNotExist

def key_required(func): # There is potentially a problem here if the login is correct but the user is not the owner of what they try to access 
    @wraps(func)
    def decorated_func(*args, **kwargs):
        correct_key = User.objects(username=kwargs['username']).first().key
        if correct_key == request.headers['X-API-KEY']:
            return func(*args, **kwargs)
        else:
            abort(401)
    return decorated_func


class TournamentResource(Resource):
    def get(self, username: str, tournament_id: str):
        tournament = Tournament.objects(tournament_id=tournament_id).exclude('owner', 'id').first().to_json()
        return Response(tournament, mimetype="application/json", status=200)

    @key_required
    def delete(self, username: str, tournament_id: str):
        try:
            tournament = Tournament.objects.get(tournament_id=tournament_id).delete()
        except DoesNotExist:
            abort(404)
        return Response("OK", status=200)


class TournamentListResource(Resource):
    def get(self, username: str):
        tournaments = Tournament.objects(owner=User.objects(username=username).first()).only('tournament_id', 'tournament_name', 't_start', 't_end')
        short_tournaments = [ShortTournament.from_tournament(e) for e in tournaments]
        return jsonify(short_tournaments)

    @key_required
    def post(self, username: str):
        data = request.get_json()
        try:
            tournament = Tournament.objects.get(tournament_id=data['tournament_id'])
            tournament.update(**data)
        except DoesNotExist:
            tournament = Tournament(**data)
            tournament.owner = User.objects(username=username).first()
            tournament.save()
        return Response("OK", status=200)


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


