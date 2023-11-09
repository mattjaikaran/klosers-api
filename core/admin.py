from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import CustomUser


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


admin.site.register(CustomUser, CustomUserAdmin)
