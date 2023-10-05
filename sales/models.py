from django.db import models
from common.models import AbstractBaseModel
from core.models import CustomUser
from . import constants


class YTDStats(AbstractBaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quota_verified = models.BooleanField(default=False)
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
    quota_attainment_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    average_deal_size = models.CharField(
        max_length=100,
        choices=constants.DEAL_SIZE_CHOICES,
        default=constants.FIVE_TEN_K,
    )
    average_sales_cycle = models.CharField(
        max_length=100, choices=constants.SALES_CYCLE_CHOICES, default="<30"
    )
    industry = models.CharField(
        max_length=50, choices=constants.INDUSTRY_CHOICES, default="IT"
    )

    def __str__(self) -> str:
        return f"YTD Stats - {self.user} - Q{self.quarter} - {self.industry}"

    class Meta:
        verbose_name_plural = "YTD Stats"


class CareerStats(AbstractBaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quota_verified = models.BooleanField(default=False)
    year = models.PositiveIntegerField(default=2023)
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
    quota_attainment_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    average_deal_size = models.CharField(
        max_length=100,
        choices=constants.DEAL_SIZE_CHOICES,
        default=constants.FIVE_TEN_K,
    )
    average_sales_cycle = models.CharField(
        max_length=100, choices=constants.SALES_CYCLE_CHOICES, default="<30"
    )
    industry = models.CharField(
        max_length=50, choices=constants.INDUSTRY_CHOICES, default="IT"
    )

    def __str__(self) -> str:
        return f"Career Stat - User: {self.user} - Company: {self.company} - {self.industry}"

    class Meta:
        verbose_name_plural = "Career Stats"


class AwardRecognition(AbstractBaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True)
    text = models.CharField(max_length=512)

    def __str__(self) -> str:
        return f"AwardRecognition - {self.text} - Type: {self.type}"

    class Meta:
        verbose_name_plural = "Award Recognitions"
