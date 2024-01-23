from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import Property


class PropertyAdmin(GenericModelAdmin):
    list_display = (
        "formatted_address",
        "organization",
        "datetime_created",
    )
    search_fields = ("formatted_address",)
    ordering_fields = "-datetime_created"


admin.site.register(Property, PropertyAdmin)
