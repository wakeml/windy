from ninja import ModelSchema

from windspeed.models import Measurements


class MeasurementsIN(ModelSchema):

    class Meta:
        model = Measurements
        fields = [
            "meter_ID",
            "lat_lon",
            "timestamp",
            "wind_direction",
            "wind_speed",
        ]


class MeasurementsOUT(ModelSchema):
    class Meta:
        model = Measurements
        fields = [
            "meter_ID",
            "lat_lon",
            "timestamp",
            "wind_direction",
            "wind_speed",
        ]
