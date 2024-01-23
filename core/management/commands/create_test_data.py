import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creating test data. Creating an organization, team, and user."
    print(">>> python manage.py create_test_data.py")

    def handle(self, *args, **kwargs):
        print(f">>> python manage.py create_test_data.py")
