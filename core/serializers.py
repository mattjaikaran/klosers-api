from core.emails import send_intro_email
from .models import CustomUser, Intro, Reference
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError
from django.contrib.auth import login

from rest_framework import serializers, exceptions
from rest_framework.authtoken.models import Token

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class ReferenceSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = Reference
        fields = ("id", "first_name", "last_name", "email", "phone", "user_id")

    def create(self, validated_data):
        print(f"validated_data in ReferenceSerializer => {validated_data}")
        try:
            reference = Reference.objects.create(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                phone=validated_data["phone"],
            )
            print(f"reference in ReferenceSerializer => {reference}")
            # get user and add reference to user
            user = CustomUser.objects.get(id=validated_data["user_id"])
            print(f"user in ReferenceSerializer => {user}")
            user.references.add(reference)
            user.save()
            return reference
        except Exception as e:
            raise ValidationError(str(e))


class CustomUserSerializer(serializers.ModelSerializer):
    references = ReferenceSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "img_url",
            "is_sales_rep",
            "is_staff",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "user_status",
            "profile_visibility",
            "market_type",
            "all_time_revenue",
            "linkedin_profile",
            "user_fit_score",
            "leaderboard_access",
            "about",
            "title",
            "company",
            "references",
        )

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validate_data):
        user = CustomUser.objects.create_user(
            validate_data["username"],
            validate_data["first_name"],
            validate_data["last_name"],
            validate_data["email"],
            validate_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, required=True)
    password = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = CustomUser
        fields = "__all__"
        exclude = ("password",)

    def validate(self, data):
        print(f"data in validate => {data}")
        try:
            user = CustomUser.objects.get(email=data["email"])
            print(f"user in validate UserLoginSerializer => {user}")
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("User does not exist")
        return data

    def validate_email(self, value):
        """Emails are always stored and compared in lowercase."""
        return value.lower()

    @staticmethod
    def login(user, request):
        """
        Log-in user and append authentication token to serialized response.
        """
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        auth_token, token_created = Token.objects.get_or_create(user=user)
        serializer = CustomUserSerializer(user, context={"request": request})
        response_data = serializer.data
        response_data["token"] = auth_token.key
        return response_data


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, value):
        email = get_adapter().clean_email(value)
        print(f"email in validate_email => {email}")
        # if allauth_settings.UNIQUE_EMAIL:
        #     if email and email_address_exists(email):
        #         raise serializers.ValidationError(
        #             _("A user is already registered with this e-mail address.")
        #         )
        return email

    def validate_password1(self, value):
        return get_adapter().clean_password(value)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError(("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user


# When a user clicks on the Request Intro button on the leaderboard,
# the user id of the stat will send to the back end along with the logged in user's data
# The back end will create a new intro object and send an email to the reference


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = (
            "id",
            "user_to",
            "user_from",
            "message",
            "accepted",
            "accepted_date",
            "declined",
            "declined_date",
            "datetime_created",
        )

    # wip email notification
    def create(self, validated_data):
        print(f"validated_data in IntroSerializer => {validated_data}")
        try:
            intro = Intro.objects.create(
                user_from=validated_data["user_from"],
                user_to=validated_data["user_to"],
                message=validated_data["message"],
            )
            print(f"intro in IntroSerializer => {intro}")

            # send email wip
            # context = {
            #     "user_first_name": validated_data["user_from"].first_name,
            #     "user_last_name": validated_data["user_from"].last_name,
            #     "message": validated_data["message"],
            # }
            # send_intro_email(context)

            return intro
        except Exception as e:
            raise ValidationError(str(e))
