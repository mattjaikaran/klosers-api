from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import CustomUser, Reference


class CustomUserAdmin(GenericModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "id",
    )
    readonly_fields = ("password", "id", "is_superuser")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    exclude = ("password",)


class ReferenceAdmin(GenericModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Reference, ReferenceAdmin)
