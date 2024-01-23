# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from .models import Organization, Team

# User = get_user_model()


# class CustomUserModelTest(TestCase):
#     def test_create_user(self):
#         user = User.objects.create_user(
#             email="test@example.com",
#             password="testpassword",
#             first_name="John",
#             last_name="Doe",
#         )
#         self.assertEqual(user.email, "test@example.com")
#         self.assertTrue(user.check_password("testpassword"))
#         self.assertEqual(user.full_name, "John Doe")
#         self.assertFalse(user.is_superuser)

#     def test_create_superuser(self):
#         admin = User.objects.create_superuser(
#             email="admin@example.com",
#             password="adminpassword",
#             first_name="Admin",
#             last_name="User",
#         )
#         self.assertEqual(admin.email, "admin@example.com")
#         self.assertTrue(admin.check_password("adminpassword"))
#         self.assertEqual(admin.full_name, "Admin User")
#         self.assertTrue(admin.is_superuser)
#         self.assertTrue(admin.is_staff)


# class OrganizationModelTest(TestCase):
#     def test_create_organization(self):
#         user = User.objects.create_user(
#             email="owner@example.com",
#             password="ownerpassword",
#             first_name="Owner",
#             last_name="User",
#         )
#         organization = Organization.objects.create(
#             name="Test Organization",
#             owner=user,
#             is_developer=True,
#         )
#         self.assertEqual(organization.name, "Test Organization")
#         self.assertEqual(organization.owner, user)
#         self.assertTrue(organization.is_developer)
#         self.assertFalse(organization.is_vendor)
#         self.assertFalse(organization.is_consultant)


# class TeamModelTest(TestCase):
#     def test_create_team(self):
#         user = User.objects.create_user(
#             email="member@example.com",
#             password="memberpassword",
#             first_name="Member",
#             last_name="User",
#         )
#         organization = Organization.objects.create(
#             name="Test Organization",
#             owner=user,
#             is_developer=True,
#         )
#         team = Team.objects.create(name="Test Team", organization=organization)
#         team.members.add(user)

#         self.assertEqual(team.name, "Test Team")
#         self.assertEqual(team.organization, organization)
#         self.assertTrue(user in team.members.all())
