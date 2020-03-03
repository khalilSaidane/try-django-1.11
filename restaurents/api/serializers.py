from rest_framework import serializers

from restaurents.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'slug',
            'location',
            'category',
            'timestamp'
        ]
