from django.test import TestCase

from properties.models import Property
from .models import Proposal, ProposalFile, RFP, Category, Stakeholder
from core.models import CustomUser, Organization


class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            name="Test Category",
            tagline="Category description",
        )
        self.assertEqual(str(category), "Category: Test Category")


class StakeholderModelTest(TestCase):
    def test_stakeholder_creation(self):
        organization = Organization.objects.create(name="Test Organization")
        stakeholder = Stakeholder.objects.create(
            first_name="John",
            last_name="Doe",
            role="Manager",
            email="john@example.com",
            organization=organization,
        )
        self.assertEqual(str(stakeholder), "Stakeholder: John Doe")


class ProposalModelTest(TestCase):
    def test_proposal_creation(self):
        user = CustomUser.objects.create_user(
            email="user@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        proposal = Proposal.objects.create(
            owner=user,
            title="Test Proposal",
            description="This is a test proposal.",
            status="Draft",
        )
        self.assertEqual(str(proposal), "Test Proposal - John Doe")


class ProposalFileModelTest(TestCase):
    def test_proposal_file_creation(self):
        user = CustomUser.objects.create_user(
            email="user@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        proposal = Proposal.objects.create(
            owner=user,
            title="Test Proposal",
            description="This is a test proposal.",
            status="Draft",
        )
        proposal_file = ProposalFile.objects.create(
            proposal=proposal,
            file="testfile.pdf",
        )
        self.assertEqual(
            str(proposal_file), f"Test Proposal - Files: {proposal_file.id}"
        )


class RFPModelTest(TestCase):
    def test_rfp_creation(self):
        user = CustomUser.objects.create_user(
            email="user@example.com",
            password="password",
            first_name="John",
            last_name="Doe",
        )
        category = Category.objects.create(name="Test Category")
        stakeholder = Stakeholder.objects.create(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
        )
        organization = Organization.objects.create(name="Test Organization")
        property = Property.objects.create(
            name="Test Property",
            formatted_address="123 Main St",
            lat=42.12345,
            long=-72.54321,
            use_types="Commercial",
            build_type="Existing Build",
            size=1000,
            size_unit="SQ FT",
            organization=organization,
        )
        proposal = Proposal.objects.create(
            owner=user,
            title="Test Proposal",
            description="This is a test proposal.",
            status="Draft",
        )
        rfp = RFP.objects.create(
            owner=user,
            name="Test RFP",
            objective="Test objective",
            requirements="Test requirements",
            timeline="Test timeline",
            tags_keywords="test, keywords",
            status="Active",
        )
        rfp.categories.add(category)
        rfp.stakeholders.add(stakeholder)
        rfp.properties.add(property)
        rfp.proposals.add(proposal)
        self.assertEqual(str(rfp), "Test RFP")
