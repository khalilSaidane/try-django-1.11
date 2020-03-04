from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from restaurents.models import Restaurant
from accounts.api.serializers import UserRetrieveSerializer
retrieve_url = HyperlinkedIdentityField(
       view_name='restaurants-api:detail',
       lookup_field='slug',
    )
delete_url = HyperlinkedIdentityField(
        view_name='restaurants-api:delete',
        lookup_field='slug',
    )


class RestaurantListSerializer(ModelSerializer):
    url = retrieve_url
    user = SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            'url',
            'user',
            'name',
            'location',
            'category',
        ]

    def get_user(self, obj):
        return str(obj.user.username)


class RestaurantRetrieveSerializer(ModelSerializer):
    delete_url = delete_url
    user = UserRetrieveSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            'user',
            'delete_url',
            'name',
            'slug',
            'location',
            'category',
        ]


class RestaurantCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'location',
            'category',
        ]