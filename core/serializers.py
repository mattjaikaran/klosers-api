from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, exceptions, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, authenticate
from core.emails import send_intro_email, send_reference_email, send_support_email
from core.models import CustomUser, ContactSupport, Intro, Reference


class ReferenceSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(required=False)

    class Meta:
        model = Reference
        fields = ("id", "first_name", "last_name", "email", "phone", "user_id")

    def create(self, validated_data):
        print(f"validated_data in ReferenceSerializer => {validated_data}")
        try:
            first_name = validated_data["first_name"]
            last_name = validated_data["last_name"]
            email = validated_data["email"]
            phone = validated_data["phone"]
            user_id = validated_data["user_id"]

            reference = Reference.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
            )
            print(f"reference in ReferenceSerializer => {reference}")
            # get user and add reference to user
            user = CustomUser.objects.get(id=user_id)
            print(f"user in ReferenceSerializer => {user}")
            user.references.add(reference)

            context = {
                "user_email": email,
                "reference_first_name": first_name,
                "user_first_name": user.first_name,
                "username": user.username,
            }
            send_reference_email(context)

            user.save()
            return reference
        except Exception as e:
            raise ValidationError(str(e))


class UserSerializer(serializers.ModelSerializer):
    references = ReferenceSerializer(many=True)

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


# class OrganizationSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True)
#     # owner = serializers.PrimaryKeyRelatedField(
#     #     queryset=CustomUser.objects.all(), required=True
#     # )

#     class Meta:
#         model = Organization
#         fields = "__all__"

#     def create(self, validated_data):
#         print(f"validated_data => {validated_data}")
#         print(f"self => {self}")
#         organization = Organization.objects.create(
#             name=validated_data["name"],
#             owner=validated_data["owner"],
#         )
#         print(f"organization => {organization}")
#         organization.save()
#         return organization


# class TeamSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True)
#     organization = serializers.PrimaryKeyRelatedField(
#         queryset=Organization.objects.all(), required=True
#     )

#     class Meta:
#         model = Team
#         fields = "__all__"

#     def create(self, validated_data):
#         print(f"validated_data => {validated_data}")
#         print(f"self => {self}")
#         team = Team.objects.create(
#             name=validated_data["name"],
#             organization=validated_data["organization"],
#         )
#         print(f"team => {team}")
#         team.save()
#         return team


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer class to register users.
    This is an organization level sign up.

    TBD -
    Meaning the user will be the owner of the organization.
    And the organization will have a default team upon signup.
    Users can be added to the team later.
    Users can be added to multiple teams later.
    """

    email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    # organizations = OrganizationSerializer(many=True, required=False)
    # teams = TeamSerializer(many=True, required=False)

    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_password(self, password):
        validate_password(password)
        return password

    def create(self, validated_data):
        try:
            # Create a CustomUser
            user = CustomUser.objects.create(
                email=validated_data["email"],
                username=validated_data["username"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
            )
            user.set_password(validated_data["password"])

            # Create an Organization
            # organization = Organization.objects.create(
            #     name=company_name,
            #     owner=user,
            # )
            # user.organizations.add(organization)

            user.save()

            return user
        except Exception as e:
            return Response(
                data={f"Error in UserRegistrationSerializer - {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def update(self, instance, validated_data):
        try:
            instance = super().update(instance, validated_data)
            return instance
        except Exception as e:
            return Response(
                data={f"Error in UserRegistrationSerializer - {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLoginSerializer(TokenObtainPairSerializer):
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

    @classmethod
    def get_token(cls, user):
        token = super(UserLoginSerializer, cls).get_token(user)
        print(f"token in get_token => {token}")

        # Add custom claims
        token["email"] = user.email

        return token

    @staticmethod
    def login(user, request):
        """
        Log-in user and append authentication token to serialized response.
        """
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        auth_token, token_created = Token.objects.get_or_create(user=user)
        print(f"auth_token in login => {auth_token}")
        serializer = UserSerializer(user, context={"request": request})
        response_data = serializer.data
        print(f"response_data in login => {response_data}")
        response_data["token"] = auth_token.key
        return response_data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)


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

    def create(self, validated_data):
        print(f"validated_data in IntroSerializer => {validated_data}")
        try:
            intro = Intro.objects.create(
                user_from=validated_data["user_from"],
                user_to=validated_data["user_to"],
                message=validated_data["message"],
            )
            print(f"intro in IntroSerializer => {intro}")

            # send email to user_to
            context = {
                "user_first_name": validated_data["user_from"].first_name,
                "user_last_name": validated_data["user_from"].last_name,
                "message": validated_data["message"],
            }
            send_intro_email(context)

            return intro
        except Exception as e:
            raise ValidationError(str(e))


class ContactSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSupport
        fields = "__all__"

    def create(self, validated_data):
        print(f"validated_data", validated_data)
        try:
            email = validated_data["email"]
            description = validated_data["description"]
            print(f"email => {email}")
            print(f"description => {description}")
            contact_support = ContactSupport.objects.create(
                email=email,
                description=description,
            )
            # send email to support team
            context = {
                "user_email": email,
                "message": description,
            }
            send_support_email(context)
            return contact_support
        except Exception as e:
            print(f"Exception create in ContactSupportSerializer => {e}")
            raise exceptions.ValidationError(f"Contact Support failed. => {e}")
