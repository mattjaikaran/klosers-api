# Generated by Django 4.2.3 on 2023-12-11 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Intro",
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
                ("message", models.TextField(blank=True, max_length=512)),
                ("accepted", models.BooleanField(default=False)),
                ("declined", models.BooleanField(default=False)),
                ("accepted_date", models.DateTimeField(blank=True, null=True)),
                ("declined_date", models.DateTimeField(blank=True, null=True)),
                (
                    "user_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_intros",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_to_intros",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="customuser",
            name="intros",
            field=models.ManyToManyField(blank=True, to="core.intro"),
        ),
    ]
