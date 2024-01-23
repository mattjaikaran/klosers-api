from operator import truediv
from rest_framework.response import Response
from rest_framework import serializers, status
from core.emails import (
    send_proposal_create_email,
    send_rfp_create_email,
    send_stakeholder_create_email,
)
from core.models import CustomUser
from core.serializers import UserSerializer
from notifications.constants import NEW_PROPOSAL
from notifications.models import Notification
from properties.serializers import PropertySerializer
from .models import RFP, Category, Proposal, ProposalFile, Stakeholder


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]


class StakeholderSerializer(serializers.ModelSerializer):
    rfp = serializers.PrimaryKeyRelatedField(queryset=RFP.objects.all(), required=False)

    class Meta:
        model = Stakeholder
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
            "rfp",
        )
        read_only_fields = ["id"]

    def create(self, validated_data):
        print(f"validated_data => {validated_data}")
        try:
            stakeholder = Stakeholder.objects.create(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                email=validated_data["email"],
                phone_number=validated_data["phone_number"],
                role=validated_data["role"],
            )
            # add stakeholder to rfp
            rfp = validated_data["rfp"]
            print(f"rfp => {rfp}")
            rfp.stakeholders.add(stakeholder)

            # send email to support team
            print(f"rfp.owner.email => {rfp.owner.email}")
            stakeholder_full_name = (
                f'{validated_data["first_name"]} {validated_data["last_name"]}'
            )
            print(f"stakeholder_full_name => {stakeholder_full_name}")
            context = {
                "user_email": rfp.owner.email,
                "stakeholder_name": stakeholder_full_name,
            }
            send_stakeholder_create_email(context)

            rfp.save()

            return stakeholder
        except Exception as e:
            print(f"error in stakeholder create => {str(e)}")
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class RFPSerializer(serializers.ModelSerializer):
    owner = UserSerializer(required=False)
    categories_data = CategorySerializer(many=True, required=False)
    stakeholders = StakeholderSerializer(many=True, required=False)
    properties = PropertySerializer(many=True, required=False)

    class Meta:
        model = RFP
        fields = (
            "id",
            "owner",
            "name",
            "objective",
            "tags_keywords",
            "requirements",
            "schedule",
            "deadline",
            "status",
            "categories",
            "categories_data",
            "stakeholders",
            "properties",
            "datetime_created",
        )
        read_only_fields = ["-datetime_created"]

    def create(self, validated_data):
        print(f"validated_data RFPSerializer => {validated_data}")
        try:
            categories = validated_data["categories"]
            rfp = RFP.objects.create(
                owner=validated_data["owner"],
                name=validated_data["name"],
                objective=validated_data["objective"],
                tags_keywords=validated_data["tags_keywords"],
                requirements=validated_data["requirements"],
                schedule=validated_data["schedule"],
                deadline=validated_data["deadline"],
                status=validated_data["status"],
            )
            # add categories to rfp
            rfp.categories.set(categories)

            # create an email notification for support team
            print(f'validated_data["owner"] => {validated_data["owner"]}')
            print(f'validated_data["owner"].email => {validated_data["owner"].email}')
            if validated_data["owner"].email is not None:
                owner_email = validated_data["owner"].email
            else:
                owner_email = CustomUser.objects.get(id=validated_data["owner"])
            print(f"owner_email => {owner_email}")
            context = {
                "user_email": owner_email,
                "rfp_name": validated_data["name"],
            }
            send_rfp_create_email(context)

            # create notification for NEW_PROJECT/RFP
            # TODO: notification recipient is users of an organization
            # that has a category that matches the rfp categories

            rfp.save()

            return rfp
        except Exception as e:
            print(f"error in rfp create => {str(e)}")
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    # def update needs to include the add the notifiation project update


class ProposalSerializer(serializers.ModelSerializer):
    rfp = serializers.PrimaryKeyRelatedField(queryset=RFP.objects.all(), required=False)
    owner = UserSerializer(required=False)

    class Meta:
        model = Proposal
        fields = (
            "id",
            "owner",
            "title",
            "description",
            "status",
            "rfp",
            "datetime_created",
        )
        # read_only_fields = ["id"]

    def create(self, validated_data):
        print(f"validated_data create ProposalSerializer => {validated_data}")
        try:
            print(f"owner => {validated_data['owner']}")
            proposal = Proposal.objects.create(
                owner=validated_data["owner"],
                title=validated_data["title"],
                description=validated_data["description"],
                status=validated_data["status"],
                rfp=validated_data["rfp"],
            )
            print(f"proposal created => {proposal}")
            rfp = validated_data["rfp"]
            print(f"rfp => {rfp}")
            print(f"rfp.owner => {rfp.owner}")

            # create notification for NEW_PROPOSAL
            rfp_owner = (
                rfp.owner
                if rfp.owner.email is not None
                else CustomUser.objects.get(id=rfp.owner)
            )
            print(f"rfp_owner => {rfp_owner}")
            notification = Notification.objects.create(
                recipient=rfp_owner,
                type=NEW_PROPOSAL,
                proposal=proposal,
            )
            print(f"notification created => {notification}")

            # attach proposal to rfp
            rfp.proposals.add(proposal)
            print(f"rfp.proposals => {rfp.proposals}")
            rfp.save()

            # send email to support team
            context = {
                "user_email": validated_data["owner"].email,
                "proposal_name": validated_data["title"],
            }
            send_proposal_create_email(context)

            return proposal
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class ProposalFileSerializer(serializers.ModelSerializer):
    proposal = serializers.PrimaryKeyRelatedField(
        queryset=Proposal.objects.all(), required=True
    )
    file = serializers.FileField()

    class Meta:
        model = ProposalFile
        fields = (
            "id",
            "file",
            "proposal",
            "datetime_created",
        )
        read_only_fields = ["id"]

    def create(self, validated_data):
        print(f"validated_data ProposalFileSerializer => {validated_data}")
        print(f"validated_data ProposalFileSerializer => {validated_data['file']}")
        try:
            proposal_file = ProposalFile.objects.create(
                proposal=validated_data["proposal"],
                file=validated_data["file"],
            )
            print(f"proposal_file => {proposal_file}")
            proposal_file.save()

            return proposal_file
        except Exception as e:
            print(f"error in proposal file create ProposalFileSerializer => {str(e)}")
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
