from django.apps import AppConfig
from geojson_pydantic import Point
from ninja.orm import fields


class WindspeedConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "windspeed"

    # # Needed to hack in support for Pointfield in django-ninja
    # def ready(self):
    #     fields.TYPES.update({"PointField": Point})
    #     return super().ready()

