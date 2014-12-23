import unittest
from mock import MagicMock
import json
import requests
import responses
import checkmate


class TestProperties(unittest.TestCase):
    def setUp(self):
        cm = checkmate.CheckMate(api_key='12345',
                                 api_base='http://partners.checkmate.dev')
        self.properties_client = cm.properties
        self.property_response = {
            'id': 123,
            'name': 'New Hotel'
        }
        self.search_params = {
            'name': 'New Hotel',
            'phone': '15555555555',
            'address': {
                'street': '1625 Main St',
                'city': 'San Francisco',
                'region': 'CA',
                'postal_code': '94115',
                'country_code': 'US'
            }
        }

    @responses.activate
    def test_search(self):
        url = 'http://partners.checkmate.dev/properties'
        responses.add(responses.GET, url,
                      body=json.dumps(self.property_response), status=200,
                      content_type='application/json')

        property = self.properties_client.search(self.search_params)
        self.assertTrue(property.id == 123)
