from django.shortcuts import render
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework import (
    viewsets,
    generics,
    status,
    mixins,
    permissions,
)
from rest_framework.response import Response

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from .models import CustomUser
from .serializers import CustomUserSerializer, UserLoginSerializer


class GenericViewSetNoDestroy(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    # we perform soft delete for all the models
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_removed = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def index(request):
#     return render(request, "index.html")


class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        """
        Validate user credentials, login, and return serialized user + auth token.
        """
        serializer = self.serializer_class(data=request.data)
        print(f"serializer => {serializer}")
        serializer.is_valid(raise_exception=True)

        print(f"serializer.data => {serializer.data}")

        # If the serializer is valid, then the email/password combo is valid.
        # Get the user entity, from which we can get (or create) the auth token
        user = authenticate(**serializer.validated_data)
        print(f"user UserLoginView => {user}")
        if user is None:
            return Response(
                data={
                    "result": "Failed",
                    "message": "Incorrect email and password combination. Please try again.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_data = UserLoginSerializer.login(user, request)
        return Response(response_data, status=status.HTTP_202_ACCEPTED)


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    authentication_classes = ()
    permission_classes = ()

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class GoogleLoginView(SocialLoginView):
    # make sure to override allowed origins in settings.py for prod
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:3000/"  # front end
    client_class = OAuth2Client
