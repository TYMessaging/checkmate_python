import requests
from attrdict import AttrDict

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json


class ApiRequester:
    def __init__(self, api_key, api_base):
        self.api_key = api_key
        self.api_base = api_base
        self.session = requests.session()
        self.session.headers.update({
            'X-CheckMate-API-Token': self.api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })

    def request(self, method, url, params={}):
        payload = json.dumps(params)
        response = self.session.request(method,
                                        self._request_uri(url),
                                        data=payload)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()

        result = response.json()

        if isinstance(result, list):
            return map(lambda r: AttrDict(r), result)
        else:
            return AttrDict(result)

    def _request_uri(self, url):
        return '{root}{url}'.format(root=self.api_base, url=url)
