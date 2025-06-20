from datetime import datetime

from django.contrib.gis.geos import Point
from django.utils import timezone

from windspeed.models import Measurements


def create_single_test_measurement(
    lat_lon: list | None,
    timestamp: datetime | None,
    tags: list | None,
    wind_direction: int = 100,
    wind_speed: float = 12.0,
):

    if timestamp is None:
        timestamp = timezone.now()

    if lat_lon is None:
        lat_lon = [41.94830673751509, -87.65555532334828]

    if tags is None:
        tags = []

    resp = Measurements.objects.create(
        lat_lon=Point(lat_lon),
        timestamp=timestamp,
        wind_direction=wind_direction,
        wind_speed=wind_speed,
        tags=tags,
    )

    return resp


def create_multiple_measurements():
    pass
