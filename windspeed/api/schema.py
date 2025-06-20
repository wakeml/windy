import json

from django.contrib.gis.geos import Point
from ninja import ModelSchema, Schema
from ninja.orm import register_field
from ninja.orm.fields import TYPES

from windspeed.models import Measurements

# class PointClass(Point):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, v, *args, **kwargs):
#         return cls(v)
#
#     @classmethod
#     def __get_pydantic_json_schema__(cls, field_schema):
#         field_schema.update(type="tuple", example=(22.5, 22.5))
#
#     def __repr__(self):
#         return f"PointField({super().__repr__()})"
#
#
# TYPES.update({"PointField": PointClass})


class MeasurementsIN(ModelSchema):
    lat_lon: list[float, float]

    class Meta:
        model = Measurements
        fields = [
            # "lat_lon",
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


class Error(Schema):
    message: str


class Success(Schema):
    message: str
