from django.db import models
from django.utils.translation import gettext_lazy as _

from .base.timestamped_model import TimestampedModel

__all__ = ["Device", "DeviceQuerySet"]


class DeviceQuerySet(models.QuerySet["Device"]):
    ...


class Device(TimestampedModel):

    objects = DeviceQuerySet.as_manager()

    class Meta:
        app_label = "app"
        verbose_name = _("device")
        verbose_name_plural = _("devices")
