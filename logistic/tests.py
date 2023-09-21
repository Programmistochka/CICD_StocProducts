from rest_framework.test import APIClient
from unittest import TestCase


class TestRequest(TestCase):
    def test_successful_request(self):
        url = '/api/v1/products/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)