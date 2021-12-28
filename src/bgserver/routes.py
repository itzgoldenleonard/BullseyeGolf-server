from .resources import *
from .dataclass import read

def initialize_routes(api):
    api_key = read('/bullseyegolf/credentials/admin_key')

    api.add_resource(UserTournament, '/user/<db_id>')
    api.add_resource(Admin, f'/admin/{api_key}/<db_id>')
    api.add_resource(UserHole, '/user/<db_id>/<int:hole_number>')
