from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import AwardRecognition, YTDStats, CareerStats


class YTDStatsAdmin(GenericModelAdmin):
    list_display = ("title", "quarter", "market", "datetime_created")
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


class CareerStatsAdmin(GenericModelAdmin):
    list_display = (
        "__str__",
        "year",
        "company",
        "industry",
        "quota_verified",
        "datetime_created",
    )
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


class AwardRecognitionAdmin(GenericModelAdmin):
    list_display = ("text", "datetime_created")
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


admin.site.register(YTDStats, YTDStatsAdmin)
admin.site.register(CareerStats, CareerStatsAdmin)
admin.site.register(AwardRecognition, AwardRecognitionAdmin)
