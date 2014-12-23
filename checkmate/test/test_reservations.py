import unittest
from mock import MagicMock
import json
import requests
import responses
import checkmate


class TestReservations(unittest.TestCase):
    def setUp(self):
        cm = checkmate.CheckMate(api_key='12345',
                                 api_base='http://partners.checkmate.dev')
        self.reservations_client = cm.reservations
        self.list_response = {
            'reservations': [
                {
                    'id': 121,
                    'confirmation_number': '12345'
                },
                {
                    'id': 122,
                    'confirmation_number': '12346'
                }
            ],
            'page': 1,
            'total': 2,
            'total_pages': 1,
            'links': []
        }
        self.reservation_response = {
            'id': 123,
            'confirmation_number': '12347'
        }
        self.create_params = {
            'external_id': '22234',
            'confirmation_number': 'testing12234',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'start_on': '2014-12-20',
            'end_on': '2014-12-24',
            'property': {
                'name': 'Hotel Checkmate',
                'address': {
                    'street': '123 Main St',
                    'city': 'Brooklyn',
                    'region': 'NY',
                    'postal_code': '11201',
                    'country_code': 'US'
                }
            }
        }

    @responses.activate
    def test_list(self):
        url = 'http://partners.checkmate.dev/reservations'
        responses.add(responses.GET, url,
                      body=json.dumps(self.list_response), status=200,
                      content_type='application/json')

        reservations = self.reservations_client.list()
        self.assertTrue('reservations' in reservations)
        self.assertTrue(reservations.reservations[0].id == 121)

    @responses.activate
    def test_list_unauthorized(self):
        url = 'http://partners.checkmate.dev/reservations'
        responses.add(responses.GET, url, status=401)
        self.assertRaises(requests.HTTPError, self.reservations_client.list)

    @responses.activate
    def test_list_error(self):
        url = 'http://partners.checkmate.dev/reservations'
        responses.add(responses.GET, url, status=500)
        self.assertRaises(requests.HTTPError, self.reservations_client.list)

    def test_list_url(self):
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        self.reservations_client.list()
        mocked_request.assert_called_once_with('GET', '/reservations', {})

    def test_list_url_with_property_id(self):
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        self.reservations_client.list({'property_id': 2})
        mocked_request.assert_called_once_with('GET',
                                               '/properties/2/reservations',
                                               {'property_id': 2})

    @responses.activate
    def test_create(self):
        url = 'http://partners.checkmate.dev/reservations'
        responses.add(responses.POST, url,
                      body=json.dumps(self.reservation_response), status=201,
                      content_type='application/json')
        reservation = self.reservations_client.create(self.create_params)
        self.assertEqual(reservation.id, self.reservation_response['id'])

    def test_create_url(self):
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        self.reservations_client.create(self.create_params)
        mocked_request.assert_called_once_with('POST',
                                               '/reservations',
                                               self.create_params)

    def test_create_url_with_property_id(self):
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        params = self.create_params.copy()
        del(params['property'])
        params['property_id'] = 123
        self.reservations_client.create(params)
        mocked_request.assert_called_once_with('POST',
                                               '/properties/123/reservations',
                                               params)

    @responses.activate
    def test_show(self):
        url = 'http://partners.checkmate.dev/reservations/123'
        responses.add(responses.GET, url,
                      body=json.dumps(self.reservation_response), status=200,
                      content_type='application/json')
        reservation = self.reservations_client.show(123)
        self.assertEqual(reservation.id, self.reservation_response['id'])

    @responses.activate
    def test_update(self):
        url = 'http://partners.checkmate.dev/reservations/123'
        responses.add(responses.PUT, url,
                      body=json.dumps(self.reservation_response), status=200,
                      content_type='application/json')
        update_params = {'loyalty_number': '123456789qwerty'}
        reservation = self.reservations_client.update(123, update_params)
        self.assertEqual(reservation.id, self.reservation_response['id'])

    @responses.activate
    def test_destroy(self):
        url = 'http://partners.checkmate.dev/reservations/123'
        responses.add(responses.DELETE, url,
                      status=204,
                      content_type='application/json')
        response = self.reservations_client.destroy(123)
        self.assertEqual(response, {})

    @responses.activate
    def test_bulk_create(self):
        url = 'http://partners.checkmate.dev/reservations/bulk_create'
        bulk_create_response = [self.reservation_response.copy(),
                                self.reservation_response.copy()]
        responses.add(responses.POST, url,
                      body=json.dumps(bulk_create_response),
                      status=200,
                      content_type='application/json')
        create_params = [self.create_params.copy(), self.create_params.copy()]

        response = self.reservations_client.bulk_create(create_params)
        self.assertEqual(response, bulk_create_response)

    def test_bulk_create_params(self):
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        self.reservations_client.bulk_create([])
        mocked_request.assert_called_once_with('POST',
                                               '/reservations/bulk_create',
                                               {'reservations': []})

    def test_bulk_create_params_with_callback(self):
        cb = "http://example.com/callback"
        self.reservations_client.client.request = MagicMock(name='request')
        mocked_request = self.reservations_client.client.request
        self.reservations_client.bulk_create([], cb)
        mocked_request.assert_called_once_with('POST',
                                               '/reservations/bulk_create',
                                               {
                                                   'reservations': [],
                                                   'webhook': cb
                                               })
