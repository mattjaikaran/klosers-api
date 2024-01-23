from django.contrib import admin

from common.admin import GenericModelAdmin
from .models import CustomUser, ContactSupport, Intro, Reference


class CustomUserAdmin(GenericModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
        "id",
    )
    readonly_fields = ("id", "is_superuser")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    exclude = ("password",)


class ReferenceAdmin(GenericModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "id",
        "datetime_created",
    )


class IntroAdmin(GenericModelAdmin):
    list_display = (
        "message",
        "user_to",
        "user_from",
        "id",
        "datetime_created",
    )


class ContactSupportAdmin(GenericModelAdmin):
    list_display = ("email", "description")
    search_fields = ("email", "description")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Intro, IntroAdmin)
admin.site.register(ContactSupport, ContactSupportAdmin)
