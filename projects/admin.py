from django.contrib import admin
from common.admin import GenericModelAdmin
from .models import RFP, Category, Proposal, ProposalFile, Stakeholder


class StakeholderAdmin(GenericModelAdmin):
    readonly_fields = ("id", "datetime_created")
    ordering_fields = "-datetime_created"

    list_display = (
        "first_name",
        "last_name",
        "email",
        "role",
        "phone_number",
        "organization",
        "datetime_created",
    )


class RFPAdmin(GenericModelAdmin):
    readonly_fields = ("id", "datetime_created")
    ordering_fields = "-datetime_created"

    list_display = (
        "name",
        "owner",
        "datetime_created",
    )


class CategoryAdmin(GenericModelAdmin):
    readonly_fields = ("id", "datetime_created")

    list_display = (
        "name",
        "datetime_created",
    )


class ProposalAdmin(GenericModelAdmin):
    readonly_fields = ("id", "datetime_created")
    ordering_fields = "-datetime_created"

    list_display = (
        "title",
        "owner",
        "datetime_created",
    )


class ProposalFileAdmin(GenericModelAdmin):
    readonly_fields = ("id", "datetime_created")
    ordering_fields = "-datetime_created"

    list_display = (
        "file",
        "datetime_created",
    )


admin.site.register(Stakeholder, StakeholderAdmin)
admin.site.register(RFP, RFPAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalFile, ProposalFileAdmin)
