from app import create_app
from config import Config

application = create_app('development.cfg')
Config.initialize()
