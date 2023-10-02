from rest_framework import mixins, viewsets, permissions

from .serializers import (
    AwardRecognitionSerializer,
    CareerStatsSerializer,
    YTDStatsSerializer,
)
from .models import AwardRecognition, YTDStats, CareerStats


class YTDStatsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = YTDStats.objects.all()
    # permission_classes = permissions.IsAuthenticated
    serializer_class = YTDStatsSerializer


class CareerStatsViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CareerStats.objects.all()
    # permission_classes = permissions.IsAuthenticated
    serializer_class = CareerStatsSerializer


class AwardRecognitionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = AwardRecognition.objects.all()
    # permission_classes = permissions.IsAuthenticated
    serializer_class = AwardRecognitionSerializer
