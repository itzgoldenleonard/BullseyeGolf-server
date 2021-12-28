from .resources import *

def initialize_routes(api):
 api.add_resource(OnlineTest, '/test')
