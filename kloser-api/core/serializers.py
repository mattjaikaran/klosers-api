from datetime import datetime
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError
from django.contrib.auth import login

# from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers, exceptions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator

# from rest_auth.serializers import PasswordResetSerializer

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

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


# wip
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False, required=True)
    password = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password")

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
            raise serializers.ValidationError(
                _("The two password fields didn't match.")
            )
        return data

    def get_cleaned_data(self):
        return {
            "email": self.validated_data.get("email", ""),
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
