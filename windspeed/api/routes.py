from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import HttpRequest
from ninja import Router
from ninja.pagination import paginate

from windspeed.models import Measurements

from .schema import Anem_listOUT, MeasurementsIN, MeasurementsOUT, Success

wind_router = Router()


@wind_router.post("/new", response={201: Success})
def new_measurement(request: HttpRequest, payload: MeasurementsIN):
    """Create a new measurement"""
    measurement = Measurements.objects.create(
        lat_lon=Point(payload.lat_lon),
        timestamp=payload.timestamp,
        wind_direction=payload.wind_direction,
        wind_speed=payload.wind_speed,
    )
    return 201, {"message": str(measurement.meter_ID.hex)}


@paginate
@wind_router.get("/", response=Anem_listOUT)
def list_all_measurements(request: HttpRequest):
    """
    The anemometers list endpoint should be _paginated_ and feature the
    _5 last readings and statistics_:
    daily readings, speed average, and weekly average.
    """
    return {
        "meas": Measurements.objects.all().order_by("-id")[:5],
        "stats": Measurements.objects.get_averages(),
    }


# Get single
@wind_router.get("/{meter_ID}", response=MeasurementsOUT)
def get_single_measurement_by_ID(request: HttpRequest, meter_ID: str):
    """return single measurement"""
    return Measurements.objects.get(meter_ID=meter_ID)


@wind_router.put("/{meter_ID}", response={204: Success})
def update_measurement(request: HttpRequest, meter_ID: str, payload: MeasurementsIN):

    _meas = Measurements.objects.filter(meter_ID=meter_ID).update(
        lat_lon=Point(payload.lat_lon),
        timestamp=payload.timestamp,
        wind_direction=payload.wind_direction,
        wind_speed=payload.wind_speed,
    )

    return 204, {"message": "updated successfully"}


@wind_router.delete("/{meter_ID}")
def delete_measurement(request: HttpRequest, meter_ID: str):
    """Delete a measurement by id"""
    Measurements.objects.filter(meter_ID=meter_ID).delete()
    return 200


# get distance and stats
@wind_router.get("/{lat}/{lon}/{distance}", response=list[MeasurementsOUT])
def get_all_close_by_location(request: HttpRequest, lat, lon, distance):
    """
    Add an endpoint to would give you statistics (avg)
    on anemometers reading within a certain radius
    (like 5 miles around a given coordinate)
    """
    pt = Point(float(lat), float(lon))

    ans = Measurements.objects.filter(lat_lon__distance_lte=(pt, D(mi=distance)))

    return ans


# tags
@paginate
@wind_router.get("/tag/{tags}", response=list[MeasurementsOUT])
def filter_all_measurements(request: HttpRequest, tags: str):
    return Measurements.objects.filter(tags__name__in=[tags])
