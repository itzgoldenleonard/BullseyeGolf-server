from .resources import *
from .dataclass import read

def initialize_routes(api):
    api_key = read('/bullseyegolf/credentials/admin_key')

    api.add_resource(OnlineTest, '/test')
    api.add_resource(Admin, f'/admin/{api_key}/<db_id>')
