# Generated by Django 4.2.3 on 2023-09-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0003_awardrecognition"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="careerstats",
            name="quarter",
        ),
        migrations.AddField(
            model_name="careerstats",
            name="year",
            field=models.PositiveIntegerField(default=2023),
        ),
        migrations.AlterField(
            model_name="careerstats",
            name="leaderboard_rank",
            field=models.PositiveIntegerField(null=True),
        ),
    ]