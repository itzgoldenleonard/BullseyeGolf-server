from flask import Response, request
from flask_restful import Resource


class OnlineTest(Resource):
    def get(self):
        return Response("Hello World! Now with flask-restful", status=200)

