from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import AwardRecognition, YTDStat, CareerStat
from import_export.admin import ImportExportModelAdmin


class YTDStatAdmin(ImportExportModelAdmin):
    list_display = (
        "title",
        "user",
        "quarter",
        "company",
        "market",
        "quota_verified",
        "datetime_created",
    )
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


class CareerStatAdmin(ImportExportModelAdmin):
    list_display = (
        "__str__",
        "user",
        "year",
        "company",
        "industry",
        "quota_verified",
        "datetime_created",
    )
    readonly_fields = ("id",)
    ordering_fields = "-year"


class AwardRecognitionAdmin(ImportExportModelAdmin):
    list_display = ("text", "user", "datetime_created")
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


admin.site.register(YTDStat, YTDStatAdmin)
admin.site.register(CareerStat, CareerStatAdmin)
admin.site.register(AwardRecognition, AwardRecognitionAdmin)
