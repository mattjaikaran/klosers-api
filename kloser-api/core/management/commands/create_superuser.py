import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create superuser locally after dropping database"
    print(f"python3 manage.py create_superuser")

    def handle(self, *args, **kwargs):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        first_name = os.environ.get("DJANGO_SUPERUSER_FIRST_NAME")
        last_name = os.environ.get("DJANGO_SUPERUSER_LAST_NAME")

        get_user_model().objects.create_superuser(
            username=username,
            email=email,
            password=password,
            # first_name=first_name,
            # last_name=last_name,
        )

        print(f"super user created successfully")
        print(f"Created superuser - {username} {email} {first_name} {last_name}")
