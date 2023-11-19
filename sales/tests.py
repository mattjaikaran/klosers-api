from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import CustomUser
from .models import YTDStat, CareerStat
from .serializers import YTDStatSerializer, CareerStatSerializer

# to run - python manage.py test sales_api
# wip. need to fix


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


class YTDStatViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("ytd-stats-list-create")
        self.user = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="john@example.com"
        )
        self.ytd_stats_data = {
            # Add test data for YTDStat creation
        }

    def test_create_ytd_stats(self):
        response = self.client.post(self.url, self.ytd_stats_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(YTDStat.objects.count(), 1)
        self.assertEqual(
            YTDStat.objects.get().quota_verified, self.ytd_stats_data["quota_verified"]
        )

    # Add more tests for YTDStat updates, deletions, etc. as needed


class CareerStatsViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("career-stats-list-create")
        self.user = CustomUser.objects.create(
            first_name="Jane", last_name="Smith", email="jane@example.com"
        )
        self.career_stats_data = {
            # Add test data for CareerStat creation
        }

    def test_create_career_stats(self):
        response = self.client.post(self.url, self.career_stats_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CareerStat.objects.count(), 1)
        self.assertEqual(
            CareerStat.objects.get().quota_verified,
            self.career_stats_data["quota_verified"],
        )

    # Add more tests for CareerStat updates, deletions, etc. as needed


class YTDStaterializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name="John", last_name="Doe", email="john@example.com"
        )
        self.ytd_stats_data = {
            # Add test data for YTDStat model serialization
        }
        self.serializer = YTDStatSerializer(data=self.ytd_stats_data)

    def test_valid_ytd_stats_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_ytd_stats_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(self.ytd_stats_data.keys()))

    # Add more tests for YTDStat serializer with invalid data, update tests, etc.


class CareerStatSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            first_name="Jane", last_name="Smith", email="jane@example.com"
        )
        self.career_stats_data = {
            # Add test data for CareerStat model serialization
        }
        self.serializer = CareerStatSerializer(data=self.career_stats_data)

    def test_valid_career_stats_serializer(self):
        self.assertTrue(self.serializer.is_valid())

    def test_career_stats_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(self.career_stats_data.keys()))

    # Add more tests for CareerStat serializer with invalid data, update tests, etc.
