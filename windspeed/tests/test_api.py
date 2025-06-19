from http import HTTPStatus

from django.test import TestCase
from ninja.testing import TestClient

from windspeed.api.routes import wind_router
from windspeed.models import Measurements


class AuthorTest(TestCase):
    def setUp(self):
        self.client = TestClient(wind_router)
        Measurements.objects.create()

    # Create
    def test_create(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # Retrieve
    def test_get_all(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 1)

    # Update
    def test_update(self):
        response = self.client.put("/{meter_ID}")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    # Delete
    def test_delete(self):
        response = self.client.delete("/{meter_ID}")
        self.assertEqual(response.status_code, HTTPStatus.OK)
