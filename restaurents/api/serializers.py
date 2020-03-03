from rest_framework import serializers

from restaurents.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'user',
            'name',
            'slug',
            'location',
            'category',
        ]


class RestaurantRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'user',
            'name',
            'slug',
            'location',
            'category',
        ]


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'location',
            'category',
        ]