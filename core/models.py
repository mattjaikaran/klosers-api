import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from common.models import AbstractBaseModel
from . import constants


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        normalized_email = self.normalize_email(email).lower()

        # Create user model instance & set password
        user = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Create user with superuser defaults via **extra_fields
    def create_superuser(self, email, password, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self.create_user(email, password, **extra_fields)

    class Meta:
        ordering = ("id",)


# class Organization(AbstractBaseModel):
#     name = models.CharField(max_length=255, unique=False)
#     url = models.URLField(max_length=200, blank=True)
#     owner = models.ForeignKey(
#         "CustomUser",
#         on_delete=models.PROTECT,
#         related_name="org_owner",
#         null=True,
#     )

#     def __str__(self):
#         return f"Organization: {str(self.name)}"


# class Team(AbstractBaseModel):
#     name = models.CharField(max_length=255)
#     organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     members = models.ManyToManyField("CustomUser", related_name="org_teams")

#     def __str__(self):
#         return f"Team: {str(self.name)}"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # `password` inherited from `AbstractBaseUser`
    # `is_superuser` inherited from `PermissionsMixin`
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        unique=True, error_messages={"unique": "A user with that email already exists"}
    )
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    img_url = models.URLField(null=True, blank=True)
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
    intros = models.ManyToManyField("Intro", blank=True)

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

    is_admin = models.BooleanField(
        "admin",
        default=False,
        help_text="Gives Users access to the Admin Dashboard to view all properties and all projects on the site.",
    )
    is_staff = models.BooleanField(
        "staff",
        default=False,
        help_text="Designates whether the user can log into Django Admin.",
    )
    is_superuser = models.BooleanField(default=False)

    # Users can be members of multiple organizations
    # organizations = models.ManyToManyField(
    #     Organization, related_name="user_orgs", blank=True
    # )

    # Use 'email' for the user's username
    USERNAME_FIELD = "email"

    # Prompt for these required fields when creating a user via `createsuperuser` command
    # 'email' is included automatically since it is set as USERNAME_FIELD
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = CustomUserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def token(self):
    #     """
    #     Allows us to get a user's token by calling `user.token` instead of
    #     `user.generate_jwt_token().

    #     The `@property` decorator above makes this possible. `token` is called
    #     a "dynamic property".
    #     """
    #     return self._generate_jwt_token()

    # def _generate_jwt_token(self):
    #     """
    #     Generates a JSON Web Token that stores this user's ID and has an expiry
    #     date set to 60 days into the future.
    #     """
    #     dt = datetime.now() + datetime.timedelta(days=60)

    #     token = jwt.encode(
    #         {"id": self.pk, "exp": int(dt.strftime("%s"))},
    #         settings.SECRET_KEY,
    #         algorithm="HS256",
    #     )

    #     return token.decode("utf-8")

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        ordering = ["email"]
        permissions = (("can_access_settings", "Can access settings"),)
        verbose_name = "User"
        verbose_name_plural = "Users"


class Reference(AbstractBaseModel):
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Intro(AbstractBaseModel):
    # user who is making/sending the intro
    user_from = models.ForeignKey(
        CustomUser, related_name="user_intros", on_delete=models.CASCADE
    )
    # user who is receiving the intro
    user_to = models.ForeignKey(
        CustomUser, related_name="user_to_intros", on_delete=models.CASCADE
    )

    message = models.TextField(max_length=512, blank=True)
    accepted = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
    declined_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user_from} - {self.user_to}"


class ContactSupport(AbstractBaseModel):
    email = models.EmailField()
    description = models.TextField(max_length=1500)

    class Meta:
        ordering = ["-datetime_created"]
        verbose_name_plural = "Support Messages"
