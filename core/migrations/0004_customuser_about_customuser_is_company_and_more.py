# Generated by Django 4.2.3 on 2023-10-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_customuser_options_alter_customuser_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="about",
            field=models.TextField(blank=True, max_length=512),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_company",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_sales_rep",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="leaderboard_access",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_status",
            field=models.CharField(
                choices=[
                    ("Open to New Opportunities", "Open to New Opportunities"),
                    ("Actively Looking for New Role", "Actively Looking for New Role"),
                    ("Will Take the Call", "Will Take the Call"),
                    (
                        "Not Interested in New Opportunities",
                        "Not Interested in New Opportunities",
                    ),
                ],
                default="Open to New Opportunities",
                max_length=50,
            ),
        ),
    ]