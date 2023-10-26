from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from . import constants


class CustomUserModelManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates a custom user with the given fields
        """
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(
            username,
            email,
            password=password,
        )

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
        verbose_name = "Custom User"
