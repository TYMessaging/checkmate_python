class Reservations:
    def __init__(self, client):
        self.client = client

    def list(self, params={}):
        return self.client.request('GET', self._url(params), params)

    def create(self, params={}):
        return self.client.request('POST', self._url(params), params)

    def _url(self, params={}):
        if 'property_id' in params:
            property_id = params['property_id']
            return '/properties/{id}/reservations'.format(id=property_id)
        else:
            return '/reservations'
