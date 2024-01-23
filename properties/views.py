from rest_framework import viewsets, mixins, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication

from .serializers import PropertySerializer
from .models import Property


class PropertyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Property.objects.all()
    # Permissions are restricted on:
    #   - get_queryset()
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # filterset_fields = ["status", "is_private"]
    search_fields = ["name", "formatted_address"]
    ordering_fields = ["-datetime_created"]

    def get_serializer_class(self):
        return PropertySerializer
