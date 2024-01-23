from rest_framework import mixins, viewsets, permissions
from rest_framework.authentication import SessionAuthentication

from .serializers import (
    AwardSerializer,
    StatSerializer,
)
from .models import Award, Stat


class LeaderboardViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    ordering_fields = "-average_deal_size"
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        return Stat.objects.all()


class StatViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    ordering_fields = "-datetime_created"
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        return Stat.objects.all()


class AwardViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        return Award.objects.all()
