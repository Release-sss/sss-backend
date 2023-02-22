from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ["Device", "DeviceQuerySet"]


class DeviceQuerySet(models.QuerySet["Device"]):
    ...


class Device(models.Model):
    
    objects = DeviceQuerySet.as_manager()

    class Meta:
        app_label = "app"
        verbose_name = _("device")
        verbose_name_plural = _("devices")
