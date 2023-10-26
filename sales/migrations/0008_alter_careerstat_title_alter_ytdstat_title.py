# Generated by Django 4.2.3 on 2023-10-26 03:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0007_rename_careerstats_careerstat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="careerstat",
            name="title",
            field=models.CharField(
                choices=[
                    ("Chief Revenue Officer (CRO)", "Chief Revenue Officer (CRO)"),
                    ("Chief Marketing Officer (CMO)", "Chief Marketing Officer (CMO)"),
                    ("VP of Sales", "VP of Sales"),
                    ("Head of Sales", "Head of Sales"),
                    ("Account Executive", "Account Executive"),
                    ("Sr. Account Executive", "Sr. Account Executive"),
                    ("Strategic Account Executive", "Strategic Account Executive"),
                    ("Mid Market Account Executive", "Mid Market Account Executive"),
                    ("Enterprise Account Executive", "Enterprise Account Executive"),
                    ("Director of Marketing", "Director of Marketing"),
                    ("Sr. Director of Marketing", "Sr. Director of Marketing"),
                    ("Product Marketing Manager", "Product Marketing Manager"),
                    ("Market Research Analyst", "Market Research Analyst"),
                    ("Sales Manager", "Sales Manager"),
                    (
                        "Sales Development Representative",
                        "Sales Development Representative",
                    ),
                    (
                        "Business Development Representative",
                        "Business Development Representative",
                    ),
                    ("Business Development Manager", "Business Development Manager"),
                    ("Brand Manager", "Brand Manager"),
                    ("Marketing Coordinator", "Marketing Coordinator"),
                    ("Content Strategist", "Content Strategist"),
                    ("Customer Success Manager", "Customer Success Manager"),
                    ("Sr. Customer Success Manager", "Sr. Customer Success Manager"),
                    ("Market Strategist", "Market Strategist"),
                    ("Channel Sales Manager", "Channel Sales Manager"),
                    ("Partner Manager", "Partner Manager"),
                    ("Sales Enablement Specialist", "Sales Enablement Specialist"),
                    ("Customer Experience Manager", "Customer Experience Manager"),
                    ("Data Analyst", "Data Analyst"),
                    ("User Acquisition Manager", "User Acquisition Manager"),
                    ("Demand Generation Specialist", "Demand Generation Specialist"),
                    ("SDR Manager", "SDR Manager"),
                    ("BDR Manager", "BDR Manager"),
                    ("Other", "Other"),
                ],
                default="Account Executive",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="ytdstat",
            name="title",
            field=models.CharField(
                choices=[
                    ("Chief Revenue Officer (CRO)", "Chief Revenue Officer (CRO)"),
                    ("Chief Marketing Officer (CMO)", "Chief Marketing Officer (CMO)"),
                    ("VP of Sales", "VP of Sales"),
                    ("Head of Sales", "Head of Sales"),
                    ("Account Executive", "Account Executive"),
                    ("Sr. Account Executive", "Sr. Account Executive"),
                    ("Strategic Account Executive", "Strategic Account Executive"),
                    ("Mid Market Account Executive", "Mid Market Account Executive"),
                    ("Enterprise Account Executive", "Enterprise Account Executive"),
                    ("Director of Marketing", "Director of Marketing"),
                    ("Sr. Director of Marketing", "Sr. Director of Marketing"),
                    ("Product Marketing Manager", "Product Marketing Manager"),
                    ("Market Research Analyst", "Market Research Analyst"),
                    ("Sales Manager", "Sales Manager"),
                    (
                        "Sales Development Representative",
                        "Sales Development Representative",
                    ),
                    (
                        "Business Development Representative",
                        "Business Development Representative",
                    ),
                    ("Business Development Manager", "Business Development Manager"),
                    ("Brand Manager", "Brand Manager"),
                    ("Marketing Coordinator", "Marketing Coordinator"),
                    ("Content Strategist", "Content Strategist"),
                    ("Customer Success Manager", "Customer Success Manager"),
                    ("Sr. Customer Success Manager", "Sr. Customer Success Manager"),
                    ("Market Strategist", "Market Strategist"),
                    ("Channel Sales Manager", "Channel Sales Manager"),
                    ("Partner Manager", "Partner Manager"),
                    ("Sales Enablement Specialist", "Sales Enablement Specialist"),
                    ("Customer Experience Manager", "Customer Experience Manager"),
                    ("Data Analyst", "Data Analyst"),
                    ("User Acquisition Manager", "User Acquisition Manager"),
                    ("Demand Generation Specialist", "Demand Generation Specialist"),
                    ("SDR Manager", "SDR Manager"),
                    ("BDR Manager", "BDR Manager"),
                    ("Other", "Other"),
                ],
                default="Account Executive",
                max_length=100,
            ),
        ),
    ]