from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import Award, Stat


class StatAdmin(GenericModelAdmin):
    list_display = (
        "user",
        "title",
        "quarter",
        "year",
        "quota",
        "company",
        "market",
        "quota_verified",
        "datetime_created",
    )
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


class AwardRecognitionAdmin(GenericModelAdmin):
    list_display = ("text", "type", "user", "id", "datetime_created")
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


admin.site.register(Stat, StatAdmin)
admin.site.register(Award, AwardRecognitionAdmin)
