import os
from django.conf import settings
from django.db import models
from common.models import AbstractBaseModel
from core.models import Organization
from . import constants


def get_property_path(instance, filename):
    return f"{settings.ENVIRONMENT}/properties/{instance.id}/{filename}"


class Property(AbstractBaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to=get_property_path, blank=True)
    formatted_address = models.CharField(max_length=255, blank=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    use_types = models.CharField(
        max_length=255, choices=constants.USE_TYPE_CHOICES, default=constants.COMMERCIAL
    )
    build_type = models.CharField(
        max_length=255,
        choices=constants.BUILD_TYPE_CHOICES,
        default=constants.EXISTING_BUILD,
    )
    size = models.IntegerField(default=0, blank=True)
    size_unit = models.CharField(
        max_length=255, choices=constants.PROPERTY_SIZE_CHOICES, default=constants.SQ_FT
    )
    organization = models.ForeignKey(
        Organization,
        default=None,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="properties",
    )

    def __str__(self):
        return f"Property: {self.name}"

    @property
    def image_name(self):
        return os.path.basename(self.image.name)

    class Meta:
        verbose_name_plural = "Properties"
