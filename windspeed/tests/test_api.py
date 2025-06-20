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
            "tags": "Stadiums",
        }

    # Create
    def test_create(self):
        response = self.client.post("/new", json=self.payload)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    # Retrieve all
    def test_get_all(self):
        create_single_test_measurement(None, None, tags=None)

        lat_lon_2 = [42.346708117969264, -71.09716683802934]
        create_single_test_measurement(lat_lon_2, None, tags=None)
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.data), 2)

    # Retrieve single
    def test_get_single(self):
        val = create_single_test_measurement(None, None, tags=None)
        mID = str(val.meter_ID)
        lat_lon_2 = [42.346708117969264, -71.09716683802934]
        create_single_test_measurement(lat_lon_2, timestamp=timezone.now(), tags=None)

        response = self.client.get("/{}".format(mID))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.data["meter_ID"], mID)

    # # Update
    # def test_update(self):
    #     val = create_single_test_measurement(None, None, tags=None)

    #     response = self.client.put("/{meter_ID}", )
    #     self.assertEqual(response.status_code, HTTPStatus.OK)

    # Delete
    def test_delete(self):
        val = create_single_test_measurement(None, None, tags=None)
        mID = str(val.meter_ID)

        response = self.client.delete("/{}".format(mID))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        total_objects_remaining = Measurements.objects.all().count()
        self.assertEqual(total_objects_remaining, 0)

    # Test location radius
    def test_location(self):
        val = create_single_test_measurement(None, None, tags=None)
        mID1 = str(val.meter_ID)

        lat_lon_2 = [42.346708117969264, -71.09716683802934]
        mid2 = create_single_test_measurement(
            lat_lon_2, timestamp=timezone.now(), tags=None
        )

        distance_miles_to_search = 50
        test_point1 = [40.82967313475971, -73.9262386676671]
        test_point2 = [41.829899598226916, -87.63376191405906]

        # no match
        response1 = self.client.get(
            "/{}/{}".format(test_point1, distance_miles_to_search)
        )
        self.assertEqual(response1.status_code, HTTPStatus.OK)
        self.assertEqual(len(response1.data), 0)

        # 1 match
        response2 = self.client.get(
            "/{}/{}".format(test_point2, distance_miles_to_search)
        )
        self.assertEqual(response2.status_code, HTTPStatus.OK)
        self.assertEqual(len(response2.data), 1)
        self.assertEqual(response2.data["meter_ID"], mID1)
