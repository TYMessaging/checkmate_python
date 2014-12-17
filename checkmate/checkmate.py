import requests
from attrdict import AttrDict

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

class CheckMate:
    def __init__(self, api_key=None, api_base='http://partners.checkmate.dev:3000'):
        self.api_key = api_key
        self.api_base = api_base
        self.session = requests.session()
        self.session.headers.update({
            'X-CheckMate-API-Token': self.api_key,
            'Accept': 'application/json'
        })

    def list_reservations(self):
        reservations =  self._request('GET', '/reservations').reservations
        return reservations

    def _request(self, method, url, params=None):
        if params is None: params = {}

        response = self.session.request(method, self._request_uri(url))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()           

        result = response.json()

        if isinstance(result, list):
            return [ AttrDict(r) for i in result ]
        else:
            return AttrDict(result)

    def _request_uri(self, url):
        return '%s%s' % (self.api_base, url)


