from django.db import models
from common.models import AbstractBaseModel
from core.models import CustomUser
from . import constants


# New refactored model Stat. Instead of Career and YTD Stats we have one model
class Stat(AbstractBaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quota_verified = models.BooleanField(default=False)
    year = models.PositiveIntegerField(default=2024)
    quarter = models.PositiveIntegerField(choices=constants.QUARTER_CHOICES, default=1)
    company = models.CharField(max_length=100)
    title = models.CharField(
        max_length=100,
        choices=constants.JOB_TITLE_CHOICES,
        default=constants.ACCOUNT_EXEC,
    )
    market = models.CharField(
        max_length=100,
        choices=constants.MARKET_CHOICES,
        default=constants.SMALL_BUSINESS,
    )
    quota = models.IntegerField(default=0)
    quota_attainment_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    average_deal_size = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    average_sales_cycle = models.IntegerField(null=True, blank=True)
    industry = models.CharField(
        max_length=50, choices=constants.INDUSTRY_CHOICES, default="IT"
    )

    def __str__(self) -> str:
        return f"Stat - User: {self.user} - Company: {self.company} - {self.industry}"

    # def calculate_average_deal_size(self):
    #     # Define your range and calculate the average deal size
    #     # This is just an example, replace with your own logic
    #     if self.average_deal_size >= 0 and self.average_deal_size < 1000:
    #         return self.average_deal_size
    #     elif self.average_deal_size >= 1000 and self.average_deal_size < 5000:
    #         return self.average_deal_size / 2
    #     else:
    #         return self.average_deal_size / 3

    # def calculate_average_sales_cycle(self):
    #     # Define your range and calculate the average sales cycle
    #     # This is just an example, replace with your own logic
    #     if self.average_sales_cycle >= 0 and self.average_sales_cycle < 30:
    #         return self.average_sales_cycle
    #     elif self.average_sales_cycle >= 30 and self.average_sales_cycle < 90:
    #         return self.average_sales_cycle / 2
    #     else:
    #         return self.average_sales_cycle / 3

    class Meta:
        verbose_name_plural = "Stats"

    # def save(self, *args, **kwargs):
    #     self.average_deal_size = self.calculate_average_deal_size()
    #     self.average_sales_cycle = self.calculate_average_sales_cycle()
    #     super().save(*args, **kwargs)


class Award(AbstractBaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f"Award - {self.text} - Type: {self.type}"

    class Meta:
        verbose_name_plural = "Awards"
