from django.db import models
from django.utils.translation import gettext_lazy as _

from sss.app.models.base.timestamped_model import TimestampedModel
from sss.app.models.device import Device


class AccidentAnalyticsQuerySet(models.QuerySet["AccidentAnalytics"]):
    ...


class AccidentAnalytics(TimestampedModel):
    device = models.ForeignKey(
        to=Device,
        on_delete=models.CASCADE,
        related_name="accident_analytics_set",
        related_query_name="accident_analytics",
    )

    objects = AccidentAnalyticsQuerySet.as_manager()

    class Meta:
        app_label = "app"
        verbose_name = _("accident analytics")
        verbose_name_plural = _("accident analytics")
