from rest_framework import mixins, viewsets, permissions

from .serializers import (
    AwardRecognitionSerializer,
    CareerStatSerializer,
    YTDStatSerializer,
)
from .models import AwardRecognition, YTDStat, CareerStat


class YTDStatViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = YTDStat.objects.all()
    # permission_classes = permissions.IsAuthenticated
    serializer_class = YTDStatSerializer
    ordering_fields = "-quarter"

    def get_queryset(self):
        # Filter objects by the authenticated user
        return YTDStat.objects.filter(user=self.request.user)


class CareerStatViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CareerStat.objects.all()
    # permission_classes = permissions.IsAuthenticated
    serializer_class = CareerStatSerializer
    ordering_fields = "-year"

    def get_queryset(self):
        # Filter objects by the authenticated user
        return CareerStat.objects.filter(user=self.request.user)


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

    def get_queryset(self):
        # Filter objects by the authenticated user
        return AwardRecognition.objects.filter(user=self.request.user)
