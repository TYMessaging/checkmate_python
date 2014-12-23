class Properties:
    def __init__(self, client):
        self.client = client

    def search(self, params={}):
        url = '/properties'
        property_params = {'property': params}
        return self.client.request('GET', url, property_params)
