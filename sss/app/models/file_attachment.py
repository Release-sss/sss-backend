from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ["FileAttachment", "FileAttachmentQuerySet"]


class FileAttachmentQuerySet(models.QuerySet["FileAttachment"]):
    ...


class FileAttachment(models.Model):
    content_type = models.CharField(
        verbose_name=_("파일 종류"), max_length=100, blank=True, null=True
    )

    link = models.URLField(max_length=1000)

    name = models.CharField(max_length=100, blank=True, verbose_name=_("이름"))

    size = models.PositiveIntegerField(verbose_name=_("파일 크기"), blank=True, null=True)

    objects = FileAttachmentQuerySet.as_manager()

    class Meta:
        app_label = "app"
        verbose_name = _("file attachment")
        verbose_name_plural = _("file attachments")
