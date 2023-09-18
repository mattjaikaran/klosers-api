# Generated by Django 4.2.3 on 2023-08-30 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sales", "0002_remove_careerstats_year_careerstats_industry_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AwardRecognition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("datetime_created", models.DateTimeField(auto_now_add=True)),
                ("last_edited", models.DateTimeField(auto_now=True)),
                ("is_removed", models.BooleanField(default=False)),
                ("type", models.CharField(blank=True, max_length=255)),
                ("text", models.CharField(max_length=512)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Award Recognitions",
            },
        ),
    ]