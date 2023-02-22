from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models
from django.utils import timezone

__all__ = ["TimestampedModel"]


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # `updated_at`를 항상 업데이트하도록 함.
        if "update_fields" in kwargs:
            kwargs["update_fields"] = list(
                set(list(kwargs["update_fields"]) + ["updated_at"])
            )
        return super().save(*args, **kwargs)

    if TYPE_CHECKING:
        id: int
