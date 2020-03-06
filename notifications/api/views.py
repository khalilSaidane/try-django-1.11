from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serialzers import NotificationListSerializer
from notifications.models import Notification


class NotificationAPIListView(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationListSerializer
    queryset = Notification.objects.all()
