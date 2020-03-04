from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from restaurents.models import Restaurant
from . import serializers
from rest_framework.filters import OrderingFilter, SearchFilter
from .pagination import RestaurantLimitOffsetPagination, RestaurantPageNumberPagination


class RestaurantListAPIView(generics.ListAPIView):
    serializer_class = serializers.RestaurantListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name', 'category', 'location']
    pagination_class = RestaurantPageNumberPagination

    # This method is not needed we can use the built in filter
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        queryset = Restaurant.objects.search(query)
        return queryset


class RestaurantRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantRetrieveSerializer
    lookup_field = 'slug'


class RestaurantUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantRetrieveSerializer
    lookup_field = 'slug'


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
