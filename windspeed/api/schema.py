from ninja import ModelSchema, Schema

from windspeed.models import Measurements


class MeasurementsIN(ModelSchema):
    lat_lon: list[float, float]

    class Meta:
        model = Measurements
        fields = [
            "timestamp",
            "wind_direction",
            "wind_speed",
            # "tags"
        ]


class MeasurementsOUT(ModelSchema):
    # lat_lon_point: json

    class Meta:
        model = Measurements
        fields = [
            "meter_ID",
            "timestamp",
            # "lat_lon",
            "wind_direction",
            "wind_speed",
        ]


class Anem_listOUT(Schema):
    """Return the list of measurements and the stats"""

    meas: list[MeasurementsOUT]
    stats: dict


class Error(Schema):
    message: str


class Success(Schema):
    message: str
