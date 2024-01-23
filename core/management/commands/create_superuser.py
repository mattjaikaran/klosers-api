import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create superuser locally after dropping database"
    print(">>> python manage.py create_superuser.py")

    def handle(self, *args, **kwargs):
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        first_name = os.environ.get("DJANGO_SUPERUSER_FIRST_NAME")
        last_name = os.environ.get("DJANGO_SUPERUSER_LAST_NAME")

        get_user_model().objects.create_superuser(
            email=email,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_admin=True,
            is_superuser=True,
        )
        print(">>> python manage.py create_superuser.py finished <<<")
        print(
            f"Created user for email: {email}, username: {username} - {first_name} {last_name} <<<"
        )
