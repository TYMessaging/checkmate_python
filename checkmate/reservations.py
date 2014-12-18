class Reservations:
    def __init__(self, client):
        self.client = client

    def list(self,
             page=1,
             property_id=None,
             confirmation_number=None,
             exclude_properties=False):

        params = {'page': page}
        url = '/reservations'

        if property_id is not None:
            url = '/properties/{id}/reservations'.format(id=property_id)
            params['property_id'] = property_id

        if confirmation_number is not None:
            params['confirmation_number'] = confirmation_number

        if exclude_properties:
            params['exclude_properties'] = 'true'

        return self.client._request('GET', url, params)
