from http import HTTPStatus

from django.test import TestCase
from django.utils import timezone
from ninja.testing import TestClient

from windspeed.api.routes import wind_router
from windspeed.models import Measurements

from windspeed.utils.data import create_single_test_measurement

class WindAPITest(TestCase):
    def setUp(self):
        self.client = TestClient(wind_router)
        self.payload = {
            "lat_lon": [41.94830673751509, -87.65555532334828],
            "timestamp": timezone.now(),
            "wind_direction": 270,
            "wind_speed": 8.0,
        }

    # # Create
    # def test_create(self):
    #     response = self.client.post("/new", json=self.payload)
    #     self.assertEqual(response.status_code, HTTPStatus.CREATED)

    # Retrieve
    def test_get_all(self):
        breakpoint()
        create_single_test_measurement(None, None)
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 1)

    # # Update
    # def test_update(self):
    #     response = self.client.put("/{meter_ID}")
    #     self.assertEqual(response.status_code, HTTPStatus.OK)

    # # Delete
    # def test_delete(self):
    #     response = self.client.delete("/{meter_ID}")
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
