import app
from config import Config


def get_regions_tuple():
    return zip(Config.DB_REGIONS, Config.DB_REGIONS)

