from rest_framework import serializers
from .models import AwardRecognition, YTDStats, CareerStats


class YTDStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTDStats
        fields = "__all__"


class CareerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerStats
        fields = "__all__"


class AwardRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardRecognition
        fields = "__all__"
