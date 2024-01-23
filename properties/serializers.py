from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from core.emails import send_property_create_email
from core.models import Organization
from projects.models import RFP
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), required=False
    )
    rfp = serializers.PrimaryKeyRelatedField(queryset=RFP.objects.all(), required=False)

    class Meta:
        model = Property
        fields = (
            "id",
            "name",
            "formatted_address",
            "lat",
            "long",
            "use_types",
            "build_type",
            "size",
            "size_unit",
            "image",
            "organization",
            "rfp",
            "datetime_created",
        )
        read_only_fields = [
            "id",
        ]

    # create a property and link it to the rfp
    def create(self, validated_data):
        print(f"validated_data => {validated_data}")
        try:
            property = Property.objects.create(
                name=validated_data["name"],
                formatted_address=validated_data["formatted_address"],
                lat=validated_data["lat"],
                long=validated_data["long"],
                use_types=validated_data["use_types"],
                build_type=validated_data["build_type"],
                size=validated_data["size"],
                size_unit=validated_data["size_unit"],
                organization=validated_data["organization"],
            )
            print(f"property created => {property}")
            rfp = RFP.objects.get(id=validated_data["rfp"].id)
            rfp.properties.add(property)
            rfp.save()

            # send email to support team
            context = {
                # "user_email": validated_data["owner"].email,
                "property_name": validated_data["name"],
            }
            send_property_create_email(context)

            return property
        except Exception as e:
            print(f"error in property create => {str(e)}")
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
