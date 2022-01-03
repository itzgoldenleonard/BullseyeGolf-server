import os
import json
from flask import Response, request
from flask_restful import Resource
from .dataclass import read, write, Tournament, Hole, Score, ShortTournament
import random


class Admin(Resource):
    def post(self, db_id: str):
        tournament: str = Tournament.deserialize(request.get_data(as_text=True))
        write(tournament.serialize(), f'/bullseyegolf/DB/{db_id}.json')
        return Response("OK", status=200)

    def delete(self, db_id: str):
        os.remove(f'/bullseyegolf/DB/{db_id}.json')
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
                element.scores.sort()
                write(tournament.serialize(), f'/bullseyegolf/DB/{db_id}.json')
                return Response("OK", status=200)

        return Response("Holey not found", status=404)

class TournamentList(Resource):
    def get(self):
        tournament_list: list = []
        for i in os.listdir('/bullseyegolf/DB'):
            tournament_list.append(ShortTournament.generate(i).to_dict())

        return Response(json.dumps(tournament_list), mimetype="application/json", status=200)


class GetImage(Resource):
    def get(self, image_name: str):
        with open(f'/bullseyegolf/images/{image_name}', 'rb') as file:
            return Response(file.read(), mimetype='image/*', status=200)



class UploadImage(Resource):
    def put(self):
        image_name: str = hex(random.getrandbits(32))

        if(request.content_length <= 2097152):
            if(request.content_type == 'image/jpeg' or request.content_type == 'image/png' or request.content_type == 'image/webp'):
                with open(f'/bullseyegolf/images/{image_name}', 'wb') as file:
                    file.write(request.get_data())
                    return Response(f'{image_name}', status=200)
            else:
                return Response(f'Unsupported image type {request.content_type}', status=400)
        else:
            return Response('File too large', status=413)

