from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.http import HttpRequest
from ninja import Router
from ninja.pagination import paginate


from django.contrib.gis.db.models import PointField

from windspeed.models import Measurements

from .schema import Error, MeasurementsIN, MeasurementsOUT, Success

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
@wind_router.get("/", response=list[MeasurementsOUT])
def list_all_measurements(request: HttpRequest):
    """Return All Measurements"""
    return Measurements.objects.all()


# Get single
@wind_router.get("/{meter_ID}", response=MeasurementsOUT)
def get_single_measurement_by_ID(request: HttpRequest, meter_ID: str):
    """return single measurement"""
    return Measurements.objects.get(meter_ID=meter_ID)


# @wind_router.put("/{meter_ID}")
# def update_measurement(request: HttpRequest, meter_ID: str, payload: MeasurementsIN):
#     obj = Measurements.objects.get(meter_ID=meter_ID)

#     Measurements.objects.create(
#         lat_lon=Point(payload.lat_lon),
#         timestamp=payload.timestamp,
#         wind_direction=payload.wind_direction,
#         wind_speed=payload.wind_speed,
#     )

# filter by tag
# @paginate
# @wind_router.get("/{tag}", response=list[MeasurementsOUT])
# def filter_all_measurements(request: HttpRequest, tag: list[str]):
#
#     return Measurements.objects.filter()


@wind_router.delete("/{meter_ID}")
def delete_measurement(request: HttpRequest, meter_ID: str):
    """Delete a measurement by id"""
    Measurements.objects.filter(meter_ID=meter_ID).delete()
    return 200


# get distance and stats
@wind_router.get("/{point}/{distance}", response=list[MeasurementsOUT])
def get_all_close_by_location(request: HttpRequest, point, distance):
    """Return All Measurements"""
    # return Measurements.objects.filter()

    # distance_miles_to_search = 50
    # point = PointField()  # get a point of a particular place (usually by latitude/longitude)
    # ans  = Company.objects.filter(places__point__distance_lte=(point, D(mi=distance_miles_to_search))).annotate(closest_city_id=F('places__city'))

    distance_miles_to_search = 50
    point = PointField(
        point
    )  # get a point of a particular place (usually by latitude/longitude)
    ans = Measurements.objects.filter(
        lat_lon__distance_lte=(point, D(mi=distance_miles_to_search))
    )

    return ans
