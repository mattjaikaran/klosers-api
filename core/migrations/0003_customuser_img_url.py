# Generated by Django 4.2.3 on 2023-12-13 21:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_intro_customuser_intros"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="img_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]