from rest_framework import generics

from restaurents.models import Restaurant
from . import serializers


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer


class RestaurantRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantRetrieveSerializer
    lookup_field = 'slug'


class RestaurantUpdateAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantCreateUpdateSerializer
    lookup_field = 'slug'


class RestaurantDeleteAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantRetrieveSerializer
    lookup_field = 'slug'


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantCreateUpdateSerializer
