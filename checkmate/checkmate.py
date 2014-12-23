from reservations import Reservations
from properties import Properties
from api_requester import ApiRequester

API_ROOT = 'https://partners.checkmate.io'


class CheckMate:
    def __init__(self, api_key=None, api_base=API_ROOT):
        client = ApiRequester(api_key, api_base)
        self.reservations = Reservations(client)
        self.properties = Properties(client)
