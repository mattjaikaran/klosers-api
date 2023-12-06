from rest_framework import mixins, viewsets

from .serializers import (
    AwardRecognitionSerializer,
    CareerStatSerializer,
    StatSerializer,
    YTDStatSerializer,
)
from .models import AwardRecognition, Stat, YTDStat, CareerStat


class YTDStatViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = YTDStat.objects.all()
    serializer_class = YTDStatSerializer
    ordering_fields = "-quarter"

    def get_queryset(self):
        # Filter objects by the authenticated user
        return YTDStat.objects.all()


class LeaderboardViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
    ordering_fields = "-quarter"

    def get_queryset(self):
        # Filter objects by the authenticated user
        return Stat.objects.all()


class CareerStatViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CareerStat.objects.all()
    serializer_class = CareerStatSerializer
    ordering_fields = "-year"

    def get_queryset(self):
        # Filter objects by the authenticated user
        return CareerStat.objects.filter(user=self.request.user)


# new stat
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

    def get_queryset(self):
        # Filter objects by the authenticated user
        return Stat.objects.filter(user=self.request.user)


class AwardRecognitionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AwardRecognition.objects.all()
    serializer_class = AwardRecognitionSerializer

    def get_queryset(self):
        # Filter objects by the authenticated user
        return AwardRecognition.objects.filter(user=self.request.user)
