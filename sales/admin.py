from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import AwardRecognition, Stat, YTDStat, CareerStat


# class YTDStatAdmin(GenericModelAdmin):
#     list_display = (
#         "title",
#         "user",
#         "quarter",
#         "quota",
#         "company",
#         "market",
#         "quota_verified",
#         "datetime_created",
#     )
#     readonly_fields = ("id",)
#     ordering_fields = "-datetime_created"


# class CareerStatAdmin(GenericModelAdmin):
#     list_display = (
#         "__str__",
#         "user",
#         "year",
#         "company",
#         "quota",
#         "industry",
#         "quota_verified",
#         "datetime_created",
#     )
#     readonly_fields = ("id",)
#     ordering_fields = "-year"


class StatAdmin(GenericModelAdmin):
    list_display = (
        "title",
        "user",
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
    list_display = ("text", "user", "datetime_created")
    readonly_fields = ("id",)
    ordering_fields = "-datetime_created"


# admin.site.register(YTDStat, YTDStatAdmin)
# admin.site.register(CareerStat, CareerStatAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(AwardRecognition, AwardRecognitionAdmin)
