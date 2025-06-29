import uuid
from datetime import timedelta

from django.contrib.gis.db import models
from django.db.models import Avg
from django.utils import timezone
from taggit.managers import TaggableManager


class StatsManager(models.Manager):
    def get_averages(self) -> dict:
        """Generate daily and weekly wind speed averages

        Returns:
            dict: {daily_ave, weekly_ave}
        """
        # Create some time deltas
        daily_duration = timezone.now() - timedelta(days=1)
        weekly_duration = timezone.now() - timedelta(days=7)

        # Calculate the averages
        daily_ave = Measurements.objects.filter(
            timestamp__gte=daily_duration
        ).aggregate(Avg("wind_speed"))
        weekly_ave = Measurements.objects.filter(
            timestamp__gte=weekly_duration
        ).aggregate(Avg("wind_speed"))
        return {
            "daily": daily_ave["wind_speed__avg"],
            "weekly": weekly_ave["wind_speed__avg"],
        }


class Measurements(models.Model):
    id = models.BigAutoField(primary_key=True)
    meter_ID = models.UUIDField(default=uuid.uuid4, editable=False)
    lat_lon = models.PointField()
    timestamp = models.DateTimeField(auto_now=True)
    wind_direction = models.IntegerField()
    wind_speed = models.FloatField()

    # Added for tags
    tags = TaggableManager()

    objects = StatsManager()

    class Meta:
        """We want to constrain the wind direction to compass bearings 00-359"""

        constraints = [
            models.CheckConstraint(
                check=models.Q(wind_direction__gte=1)
                & models.Q(wind_direction__lt=360),
                name="Wind Direction",
            )
        ]

    def __str__(self) -> str:
        return f"{str(self.meter_ID)}"
