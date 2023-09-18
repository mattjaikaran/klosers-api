from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import CustomUser
from .models import YTDStats, CareerStats
from .serializers import YTDStatsSerializer, CareerStatsSerializer

# to run - python manage.py test sales_api


class UserViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("user-list-create")
        self.user_data = {
            # Add test data for user creation
        }

    def test_create_user(self):
        response = self.client.post(self.url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(
            CustomUser.objects.get().first_name, self.user_data["first_name"]
        )

    def test_get_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), CustomUser.objects.count())

    # Add more tests for user updates, deletions, etc. as needed


class YTDStatsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("ytd-stats-list-create")
        self.user = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="john@example.com"
        )
        self.ytd_stats_data = {
            # Add test data for YTDStats creation
        }

    def test_create_ytd_stats(self):
        response = self.client.post(self.url, self.ytd_stats_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YTDStats.objects.count(), 1)
        self.assertEqual(
            YTDStats.objects.get().quota_verified, self.ytd_stats_data["quota_verified"]
        )

    # Add more tests for YTDStats updates, deletions, etc. as needed


class CareerStatsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("career-stats-list-create")
        self.user = CustomUser.objects.create(
            first_name="Jane", last_name="Smith", email="jane@example.com"
        )
        self.career_stats_data = {
            # Add test data for CareerStats creation
        }

    def test_create_career_stats(self):
        response = self.client.post(self.url, self.career_stats_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CareerStats.objects.count(), 1)
        self.assertEqual(
            CareerStats.objects.get().quota_verified,
            self.career_stats_data["quota_verified"],
        )

    # Add more tests for CareerStats updates, deletions, etc. as needed


class YTDStatsSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="john@example.com"
        )
        self.ytd_stats_data = {
            # Add test data for YTDStats model serialization
        }
        self.serializer = YTDStatsSerializer(data=self.ytd_stats_data)

    def test_valid_ytd_stats_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_ytd_stats_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(self.ytd_stats_data.keys()))

    # Add more tests for YTDStats serializer with invalid data, update tests, etc.


class CareerStatsSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name="Jane", last_name="Smith", email="jane@example.com"
        )
        self.career_stats_data = {
            # Add test data for CareerStats model serialization
        }
        self.serializer = CareerStatsSerializer(data=self.career_stats_data)

    def test_valid_career_stats_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_career_stats_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(self.career_stats_data.keys()))

    # Add more tests for CareerStats serializer with invalid data, update tests, etc.
