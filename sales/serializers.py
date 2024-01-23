from h11 import Response
from rest_framework import serializers, status

from core.serializers import UserSerializer
from .models import Award, Stat


class StatSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source="user", read_only=True)

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
        try:
            print(f"validated_data => {validated_data}")
            stat = Stat.objects.create(**validated_data)
            return stat
        except Exception as e:
            print(f"Error in StatSerializer.create => {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AwardSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source="user", read_only=True)

    class Meta:
        model = Award
        fields = (
            "id",
            "type",
            "text",
            "user",
            "user_data",
            "datetime_created",
        )

    def create(self, validated_data):
        try:
            print(f"validated_data => {validated_data}")
            award = Award.objects.create(**validated_data)
            return award
        except Exception as e:
            print(f"Error in AwardSerializer.create => {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
