import requests
from attrdict import AttrDict

from reservations import Reservations

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json


class CheckMate:
    def __init__(self, api_key=None,
                 api_base='http://partners.checkmate.dev:3000'):
        self.api_key = api_key
        self.api_base = api_base
        self.session = requests.session()
        self.session.headers.update({
            'X-CheckMate-API-Token': self.api_key,
            'Accept': 'application/json'
        })
        self.reservations = Reservations(self)

    def _request(self, method, url, params={}):
        response = self.session.request(method,
                                        self._request_uri(url),
                                        data=params)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        result = response.json()

        if isinstance(result, list):
            return map(lambda r: AttrDict(r), result)
        else:
            return AttrDict(result)

    def _request_uri(self, url):
        return '{root}{url}'.format(root=self.api_base, url=url)
