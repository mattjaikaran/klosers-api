from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import AwardRecognition, YTDStats, CareerStats


class YTDStatsAdmin(GenericModelAdmin):
    list_display = ("title", "quarter", "market")
    readonly_fields = ("id",)


class CareerStatsAdmin(GenericModelAdmin):
    list_display = ("__str__", "year", "company", "industry", "quota_verified")
    readonly_fields = ("id",)


class AwardRecognitionAdmin(GenericModelAdmin):
    list_display = ("text",)
    readonly_fields = ("id",)


admin.site.register(YTDStats, YTDStatsAdmin)
admin.site.register(CareerStats, CareerStatsAdmin)
admin.site.register(AwardRecognition, AwardRecognitionAdmin)
