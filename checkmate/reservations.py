class Reservations:
    def __init__(self, client):
        self.client = client

    def list(self, params={}):
        return self.client.request('GET', self._url(params), params)

    def create(self, params={}):
        return self.client.request('POST', self._url(params), params)

    def show(self, id):
        url = '/reservations/{0}'.format(id)
        return self.client.request('GET', url, {})

    def update(self, id, params={}):
        url = '/reservations/{0}'.format(id)
        update_params = {'reservation': params}
        return self.client.request('PUT', url, update_params)

    def destroy(self, id):
        url = '/reservations/{0}'.format(id)
        return self.client.request('DELETE', url, {})

    def bulk_create(self, reservations=[], webhook=None):
        url = '/reservations/bulk_create'
        params = {'reservations': reservations}
        if webhook:
            params['webhook'] = webhook
        return self.client.request('POST', url, params)

    def _url(self, params={}):
        if 'property_id' in params:
            property_id = params['property_id']
            return '/properties/{id}/reservations'.format(id=property_id)
        else:
            return '/reservations'
