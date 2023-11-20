from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

from common.models import AbstractBaseModel
from . import constants


class CustomUserModelManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates a custom user with the given fields
        """
        user = self.model(
            username=username, email=self.normalize_email(email), **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username, email, password=password, **extra_fields)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profile_visibility = models.CharField(
        max_length=10, choices=constants.VISIBILITY_CHOICES, default=constants.PUBLIC
    )
    market_type = models.CharField(max_length=100, null=True)
    all_time_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    linkedin_profile = models.URLField(null=True, blank=True)
    user_fit_score = models.IntegerField(default=0)

    # references
    references = models.ManyToManyField("Reference", blank=True)

    user_status = models.CharField(
        max_length=50,
        choices=constants.USER_STATUS_CHOICES,
        default=constants.OPEN_TO_OPPORTUNITIES,
    )

    # Sales Rep or a Company wanting access to the leaderboard
    is_sales_rep = models.BooleanField(default=True)
    is_company = models.BooleanField(default=False)
    leaderboard_access = models.BooleanField(default=False)

    about = models.TextField(max_length=512, blank=True)

    @property
    def full_name(self):
        return "{self.first_name} + {self.last_name}"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserModelManager()

    class Meta:
        verbose_name = "User"


class Reference(AbstractBaseModel):
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    @property
    def full_name(self):
        return "{self.first_name} + {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
