from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import UpdateAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from activity.models import Activity, ActivityType
from api.emails import send_email_verification
from user.mixins import ClientPermission
from user.models import Client

from api.serializers import ActivitySerializer, ChangePasswordSerializer, ActivityTypeSerializer, DeleteSerializer
from api.serializers import RegistrationSerializer


class ActivityViewSet(ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ClientPermission]


class ClientViewSet(CreateModelMixin, GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        client = serializer.save()
        url = self.request.build_absolute_uri(reverse('email_verification',
                                                      args=[client.user.id, client.token_verification]))
        send_email_verification(url, client)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
    model = User
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ClientPermission]

    def get_object(self):
        client = get_object_or_404(Client, user=self.request.user)
        return client.user


class ActivityTypeViewSet(ReadOnlyModelViewSet):
    serializer_class = ActivityTypeSerializer
    queryset = ActivityType.objects.all()


class ClientDeleteView(RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = DeleteSerializer
    model = Client
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ClientPermission]

    def get_object(self):
        client = get_object_or_404(Client, user=self.request.user)
        return client.user
