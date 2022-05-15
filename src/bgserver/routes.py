"""Endpoints"""

from .resources import *

def initialize_routes(api):
    """
    api.add_resource(UserTournament, '/user/<db_id>')
    api.add_resource(Admin, f'/admin/{api_key}/<db_id>')
    api.add_resource(UserHole, '/user/<db_id>/<int:hole_number>')
    api.add_resource(TournamentList, '/user/')
    api.add_resource(GetImage, '/image/<image_name>')
    api.add_resource(UploadImage, f'/image/{api_key}')
    """
    api.add_resource(MongoTest, '/mongo/')
