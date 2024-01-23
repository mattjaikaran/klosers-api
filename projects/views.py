from rest_framework import viewsets, mixins, permissions
from .models import RFP, Category, Proposal, ProposalFile, Stakeholder
from rest_framework.authentication import SessionAuthentication
from .serializers import (
    CategorySerializer,
    ProposalFileSerializer,
    ProposalSerializer,
    RFPSerializer,
    StakeholderSerializer,
)


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class StakeholderViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer
    permission_classes = ()
    authentication_classes = ()

    def get_queryset(self):
        queryset = Stakeholder.objects.all()
        return queryset


class ProposalViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permission_classes = ()
    authentication_classes = ()

    def get_queryset(self):
        queryset = Proposal.objects.all()
        return queryset


class ProposalFileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ProposalFile.objects.all()
    serializer_class = ProposalFileSerializer
    permission_classes = ()
    authentication_classes = ()

    def get_queryset(self):
        queryset = ProposalFile.objects.all()
        return queryset


class RFPViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = RFP.objects.all()
    serializer_class = RFPSerializer
    permission_classes = ()
    authentication_classes = ()

    def get_queryset(self):
        # allow filtering by organizationn.
        # if a user is part of an organization
        # then they can only see RFPs that belong to that organization
        queryset = RFP.objects.all()
        return queryset
