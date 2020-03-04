from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from . import serializers
from rest_framework.filters import OrderingFilter, SearchFilter

from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
    queryset = User.objects.all()
