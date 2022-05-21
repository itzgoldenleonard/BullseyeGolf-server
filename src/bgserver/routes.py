"""Endpoints"""

from .resources import *

def initialize_routes(api):
    api.add_resource(TournamentResource, '/<string:username>/<string:tournament_id>')
    api.add_resource(TournamentListResource, '/<string:username>')
