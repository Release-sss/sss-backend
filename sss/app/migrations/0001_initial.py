# Generated by Django 4.0.6 on 2023-02-22 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "device",
                "verbose_name_plural": "devices",
            },
        ),
        migrations.CreateModel(
            name="FileAttachment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_type",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="파일 종류"
                    ),
                ),
                ("link", models.URLField(max_length=1000)),
                (
                    "name",
                    models.CharField(blank=True, max_length=100, verbose_name="이름"),
                ),
                (
                    "size",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="파일 크기"
                    ),
                ),
            ],
            options={
                "verbose_name": "file attachment",
                "verbose_name_plural": "file attachments",
            },
        ),
    ]
