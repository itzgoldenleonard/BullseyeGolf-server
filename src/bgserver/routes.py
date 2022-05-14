from .resources import *
from .dataclass import read
from .generate_key import generate_key
import os

def initialize_routes(api):
    try:
        api_key = read('/bullseyegolf/credentials/admin_key')
    except FileNotFoundError:
        generate_key()
        api_key = read('/bullseyegolf/credentials/admin_key')
        print(f'No API key was found, a new one was generated:\n{api_key}')

    os.makedirs('/bullseyegolf/DB', exist_ok=True)

    api.add_resource(UserTournament, '/user/<db_id>')
    api.add_resource(Admin, f'/admin/{api_key}/<db_id>')
    api.add_resource(UserHole, '/user/<db_id>/<int:hole_number>')
    api.add_resource(TournamentList, '/user/')
    api.add_resource(GetImage, '/image/<image_name>')
    api.add_resource(UploadImage, f'/image/{api_key}')
