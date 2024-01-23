from django.test import TestCase
from .models import Property
from core.models import Organization
from . import constants


class PropertyModelTest(TestCase):
    def setUp(self):
        # Create an organization for testing
        self.organization = Organization.objects.create(name="Test Organization")

    def test_property_creation(self):
        property = Property.objects.create(
            name="Test Property",
            formatted_address="123 Main St",
            lat=45.6789,
            long=-123.4567,
            use_types=constants.COMMERCIAL,
            build_type=constants.EXISTING_BUILD,
            size=1000,
            size_unit=constants.SQ_FT,
            organization=self.organization,
        )
        self.assertEqual(str(property), "Property: Test Property")

    def test_property_image_name(self):
        property = Property.objects.create(name="Test Property")
        property.image.name = "test_image.jpg"
        self.assertEqual(property.image_name, "test_image.jpg")

    def test_property_defaults(self):
        property = Property.objects.create(name="Test Property")
        self.assertEqual(property.use_types, constants.COMMERCIAL)
        self.assertEqual(property.build_type, constants.EXISTING_BUILD)
        self.assertEqual(property.size, 0)
        self.assertEqual(property.size_unit, constants.SQ_FT)
        self.assertIsNone(property.organization)

    def test_property_with_organization(self):
        property = Property.objects.create(
            name="Test Property",
            organization=self.organization,
        )
        self.assertEqual(property.organization, self.organization)
