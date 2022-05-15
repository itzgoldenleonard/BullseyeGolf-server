from flask import Response, request
from flask_restful import Resource
from .database.models import Score

class MongoTest(Resource):
    def get(self):
        score = Score.objects().to_json()
        return Response(score, mimetype="application/json", status=200)

    def post(self):
        data = request.get_json()
        score = Score(**data).save()
        id = score.id
        return Response(str(id), status=200)
