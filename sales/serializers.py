from rest_framework import serializers
from .models import AwardRecognition, YTDStat, CareerStat


class YTDStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTDStat
        fields = "__all__"


class CareerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerStat
        fields = "__all__"


class AwardRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardRecognition
        fields = "__all__"
