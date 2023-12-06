from rest_framework import serializers
from .models import AwardRecognition, Stat, YTDStat, CareerStat


class YTDStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = YTDStat
        fields = "__all__"


class CareerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerStat
        fields = "__all__"


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = "__all__"

    def create(self, validated_data):
        print(f"validated_data => {validated_data}")
        stat = Stat.objects.create(**validated_data)
        return stat


class AwardRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardRecognition
        fields = "__all__"
