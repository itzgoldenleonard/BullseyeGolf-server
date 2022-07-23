from flask import Response, request, jsonify, abort
from flask_restful import Resource
import time
from .database.models import Tournament, User, ShortTournament, Score
from functools import wraps
from mongoengine import ValidationError

def key_required(func): # This function only checks the validity of the login, not if the user actually owns what they're trying to access
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

        try:
            if request.headers['No-Hole-Images'] == 'true' or request.headers['No-Hole-Images'] == 'True':
                try:
                    tournament = Tournament.objects(tournament_id=tournament_id).exclude('owner', 'id', 'holes__hole_image').first().to_json()
                except AttributeError:
                    abort(404, "Tournament not found")
                return Response(tournament, mimetype="application/json", status=200)
        except KeyError:
            pass

        try:
            tournament = Tournament.objects(tournament_id=tournament_id).exclude('owner', 'id').first().to_json()
        except AttributeError:
            abort(404, "Tournament not found")
        return Response(tournament, mimetype="application/json", status=200)


    @key_required
    def delete(self, username: str, tournament_id: str):
        try:
            tournament = Tournament.objects(tournament_id=tournament_id).only('owner').first()
            if tournament.owner.username == username:
                tournament.delete()
                return Response("OK", status=200)
            else:
                abort(403)
        except AttributeError:
            abort(404)


class TournamentListResource(Resource):
    def get(self, username: str):
        tournaments = Tournament.objects(owner=User.objects(username=username).first()).only('tournament_id', 'tournament_name', 't_start', 't_end')
        short_tournaments = [ShortTournament.from_tournament(e) for e in tournaments]
        return jsonify(short_tournaments)

    @key_required
    def post(self, username: str):
        data = request.get_json()
        try:
            tournament = Tournament.objects(tournament_id=data['tournament_id']).only('owner').first()
            if tournament.owner.username == username:
                tournament.update(**data)
            else:
                abort(403)
        except AttributeError:
            tournament = Tournament(**data)
            tournament.owner = User.objects(username=username).first()
            tournament.save()
        return Response("OK", status=200)


class HoleResource(Resource):
    def get(self, username: str, tournament_id: str, hole_number: int):
        tournament = Tournament.objects(tournament_id=tournament_id).only('holes').first()
        try:
            for hole in tournament.holes:
                if hole.hole_number == hole_number:
                    return Response(hole.to_json(), mimetype="application/json", status=200)
        except AttributeError:
            abort(404, "Tournament not found")
        abort(404, "Hole not found")

    def post(self, username: str, tournament_id: str, hole_number: int):
        data = request.get_json()
        score = Score(player_name=data['player_name'], player_score=data['player_score'], t=time.time())
        try:
            score.validate()
        except ValidationError:
            abort(400, "Invalid score")
        tournament = Tournament.objects(tournament_id=tournament_id, holes__hole_number=hole_number).only('holes', 't_start', 't_end')
        if not (tournament[0].t_start < int(time.time()) < tournament[0].t_end):
            abort(403)
        tournament.update(add_to_set__holes__S__scores=score)
        return Response("OK", mimetype="text/plain", status=200)


