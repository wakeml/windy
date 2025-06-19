from django.http import HttpRequest
from ninja import Router
from ninja.pagination import paginate

from windspeed.models import Measurements

from .schema import MeasurementsIN, MeasurementsOUT

wind_router = Router()


@wind_router.post("/new")
def new_measurement(request: HttpRequest, payload: MeasurementsIN):
    """Create a new measurement

    Args:
        request (HttpRequest):
        payload (MeasurementsIN): _description_

    Returns:
        _type_: _description_
    """
    resp = Measurements.objects.create(
        meter_ID=payload.meter_id,
        meter_lat_lon=payload.meter_lat_lon,
        meter_timestamp=payload.timestamp,
        wind_direction=payload.wind_direction,
        wind_speed=payload.windspeed,
    )

    return resp


@paginate
@wind_router.get("/", response=list[MeasurementsOUT])
def list_all_measurements(request: HttpRequest):
    """Return All Measurements

    Args:
        request (HttpRequest): _description_

    Returns:
        list: _description_
    """
    return Measurements.objects.all()


@paginate
@wind_router.get("/{tag}", response=list[MeasurementsOUT])
def filter_all_measurements(request: HttpRequest, tag: list[str]):

    return Measurements.objects.filter()


@wind_router.get("/{meter_ID}")
def get_author(request: HttpRequest, meter_ID: str):
    return Measurements.objects.get(meter_ID=meter_ID)


@wind_router.delete("/{meter_ID}")
def delete_author(request: HttpRequest, meter_ID: str):
    pass
