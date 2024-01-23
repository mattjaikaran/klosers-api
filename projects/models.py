import django.utils.timezone
from django.db import models
from common.models import AbstractBaseModel
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator

from core.models import CustomUser, Organization
from properties.models import Property
from . import constants


def get_category_path(instance, filename):
    return f"{settings.ENVIRONMENT}/projects/categories/{instance.id}/{filename}"


# seed cmd to load categories
# $ python3 manage.py loaddata projects/seed/categories.json --app projects --format=json
class Category(AbstractBaseModel):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, blank=True)
    icon = models.ImageField(
        max_length=255, upload_to=get_category_path, null=True, blank=True
    )

    def __str__(self):
        return f"Category: {str(self.name)}"

    class Meta:
        verbose_name_plural = "Categories"


# This receiver is necessary for the seed cmd to work properly
# or else a null value will be for datetime_created and cause an error
@receiver(pre_save, sender=Category)
def set_datetime_created_on_save(sender, instance, *args, **kwargs):
    if not instance.datetime_created:
        instance.datetime_created = django.utils.timezone.now()
        instance.last_edited = django.utils.timezone.now()


class Stakeholder(AbstractBaseModel):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    role = models.CharField(
        max_length=50,
        choices=constants.TEAM_ROLES_CHOICES,
        default=constants.OTHER,
        blank=True,
    )
    email = models.EmailField()
    phone_number_validator = RegexValidator(
        regex=r"^\d{9,15}$", message="Phone number must contain only 9 to 15 digits"
    )
    phone_number = models.CharField(
        max_length=15, blank=True, validators=[phone_number_validator]
    )
    organization = models.ForeignKey(
        Organization,
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="contacts",
    )

    def __str__(self):
        return f"Stakeholder: {self.first_name} {self.last_name}"

    class Meta:
        ordering = ["id"]


def get_proposal_files(instance, filename):
    return f"{settings.ENVIRONMENT}/proposals/{filename}"


class Proposal(AbstractBaseModel):
    # Owner - Seller/Vendor
    owner = models.ForeignKey(
        CustomUser,
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="owner",
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2560, blank=True, default="")
    status = models.CharField(
        max_length=128, choices=constants.STATUS_CHOICES, default=constants.IN_DRAFT
    )
    # saves the ID of the RFP that this proposal is associated with
    rfp = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return f"{self.title} - {self.owner}"


class ProposalFile(AbstractBaseModel):
    proposal = models.ForeignKey(
        Proposal, blank=True, related_name="proposal_files", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=get_proposal_files)

    def __str__(self):
        return f"{self.proposal.title} - Files: {self.id}"


class RFP(AbstractBaseModel):
    owner = models.ForeignKey(
        CustomUser,
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="rfp_owner",
    )
    name = models.CharField(max_length=100)
    objective = models.TextField(max_length=256, blank=True)
    requirements = models.TextField(max_length=1024, blank=True)
    schedule = models.TextField(max_length=256, blank=True)
    deadline = models.TextField(max_length=256, blank=True)
    tags_keywords = models.TextField(max_length=1024, blank=True)
    status = models.CharField(
        max_length=128, choices=constants.RFP_CHOICES, default=constants.ACTIVE
    )
    categories = models.ManyToManyField(
        Category, related_name="rfp_categories", blank=True
    )
    stakeholders = models.ManyToManyField(
        Stakeholder, blank=True, related_name="rfp_stakeholders"
    )
    properties = models.ManyToManyField(
        Property, related_name="rfp_properties", blank=True
    )
    proposals = models.ManyToManyField(
        Proposal, related_name="rfp_proposals", blank=True
    )

    class Meta:
        verbose_name_plural = "RFPs"

    def __str__(self):
        return self.name
