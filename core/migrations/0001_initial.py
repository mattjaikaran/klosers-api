# Generated by Django 4.2.3 on 2023-12-01 02:49

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reference",
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
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(blank=True, max_length=20)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
                (
                    "first_name",
                    models.CharField(max_length=50, verbose_name="First Name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=50, verbose_name="Last Name"),
                ),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("title", models.CharField(blank=True, max_length=100)),
                ("company", models.CharField(blank=True, max_length=100)),
                (
                    "profile_visibility",
                    models.CharField(
                        choices=[("PUBLIC", "Public"), ("PRIVATE", "Private")],
                        default="PUBLIC",
                        max_length=10,
                    ),
                ),
                ("market_type", models.CharField(max_length=100, null=True)),
                (
                    "all_time_revenue",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("linkedin_profile", models.URLField(blank=True, null=True)),
                ("user_fit_score", models.IntegerField(default=0)),
                (
                    "user_status",
                    models.CharField(
                        choices=[
                            ("Open to New Opportunities", "Open to New Opportunities"),
                            (
                                "Actively Looking for New Role",
                                "Actively Looking for New Role",
                            ),
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
                ("is_sales_rep", models.BooleanField(default=True)),
                ("is_company", models.BooleanField(default=False)),
                ("leaderboard_access", models.BooleanField(default=False)),
                ("about", models.TextField(blank=True, max_length=512)),
                ("active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                ("references", models.ManyToManyField(blank=True, to="core.reference")),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
            },
        ),
    ]
