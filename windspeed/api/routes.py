from django.contrib.gis.geos import Point
from django.http import HttpRequest
from ninja import Router
from ninja.pagination import paginate

from windspeed.models import Measurements

from .schema import Error, MeasurementsIN, MeasurementsOUT, Success

wind_router = Router()


@wind_router.post("/new", response={201: Success})
def new_measurement(request: HttpRequest, payload: MeasurementsIN):
    """Create a new measurement

    Args:
        request (HttpRequest):
        payload (MeasurementsIN): _description_

    Returns:
        _type_: _description_
    """
    measurement = Measurements.objects.create(
        lat_lon=Point(payload.lat_lon),
        timestamp=payload.timestamp,
        wind_direction=payload.wind_direction,
        wind_speed=payload.wind_speed,
    )
    return 201, {"message": str(measurement.meter_ID.hex)}


@paginate
@wind_router.get("/", response=list[MeasurementsOUT])
def list_all_measurements(request: HttpRequest):
    """Return All Measurements
    """
    return Measurements.objects.all()


# @paginate
# @wind_router.get("/{tag}", response=list[MeasurementsOUT])
# def filter_all_measurements(request: HttpRequest, tag: list[str]):

#     return Measurements.objects.filter()


# @wind_router.get("/{meter_ID}")
# def get_author(request: HttpRequest, meter_ID: str):
#     return Measurements.objects.get(meter_ID=meter_ID)


# @wind_router.delete("/{meter_ID}")
# def delete_author(request: HttpRequest, meter_ID: str):
#     pass
