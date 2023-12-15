from rest_framework import serializers

from core.serializers import CustomUserSerializer
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
    user_data = CustomUserSerializer(source="user", read_only=True)

    class Meta:
        model = Stat
        fields = (
            "id",
            "user",
            "user_data",
            "quota_verified",
            "quarter",
            "year",
            "company",
            "title",
            "market",
            "quota",
            "quota_attainment_percentage",
            "average_deal_size",
            "average_sales_cycle",
            "industry",
        )

    def create(self, validated_data):
        print(f"validated_data => {validated_data}")
        stat = Stat.objects.create(**validated_data)
        return stat


class AwardRecognitionSerializer(serializers.ModelSerializer):
    user_data = CustomUserSerializer(source="user", read_only=True)

    class Meta:
        model = AwardRecognition
        fields = (
            "id",
            "type",
            "text",
            "user",
            "user_data",
            "datetime_created",
        )


class LeaderboardSerializer(serializers.ModelSerializer):
    user_data = serializers.SerializerMethodField()

    class Meta:
        model = Stat
        fields = (
            "id",
            "user",
            "user_data",
            "quota_verified",
            "quarter",
            "year",
            "company",
            "title",
            "market",
            "quota",
            "quota_attainment_percentage",
            "average_deal_size",
            "average_sales_cycle",
            "industry",
        )
