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


def create_multiple_test_measurements():
    # fmt:off
    _resp = Measurements.objects.create(lat_lon=Point(41.94830673751509, -87.65555532334828), timestamp=timezone.now, wind_direction=10, wind_speed=60.0)
    _resp.tags.add("Wrigley Field")

    _resp = Measurements.objects.create(lat_lon=Point(40.829687249248764, -73.9261744999909), timestamp=timezone.now, wind_direction=20, wind_speed=88.0)
    _resp.tags.add("Yankee Stadium")

    _resp = Measurements.objects.create(lat_lon=Point(42.34668500328718, -71.09728073127724), timestamp=timezone.now, wind_direction=30, wind_speed=12.0)
    _resp.tags.add("Fenway Park")

    _resp = Measurements.objects.create(lat_lon=Point(29.68497015707123, -95.40760246092765), timestamp=timezone.now, wind_direction=40, wind_speed=33.0)
    _resp.tags.add("Houston Astrodome")

    _resp = Measurements.objects.create(lat_lon=Point(37.77838718012909, -122.38920590043773), timestamp=timezone.now, wind_direction=50, wind_speed=75.0)
    _resp.tags.add("Candlestick Park")

    _resp = Measurements.objects.create(lat_lon=Point(39.283906298985016, -76.62170472023533), timestamp=timezone.now, wind_direction=60, wind_speed=96.6)
    _resp.tags.add("Camden Yards")

    # fmt:on
