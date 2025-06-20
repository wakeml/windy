
from datetime import datetime
from windspeed.models import Measurements
from django.utils import timezone
from django.contrib.gis.geos import Point

def create_single_test_measurement(
        lat_lon: list | None,
        timestamp: datetime | None,
        wind_direction: int = 100,
        wind_speed: float = 12.0,
    ):

    if timestamp is None:
        timestamp = timezone.now()

    if lat_lon is None:
        lat_lon = [41.94830673751509, -87.65555532334828]

    resp = Measurements.objects.create(
        lat_lon = Point(lat_lon),
        timestamp = timestamp,
        wind_direction = wind_direction,
        wind_speed = wind_speed
    )

    return resp


def create_multiple_measurements():
    pass


