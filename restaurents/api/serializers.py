from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from restaurents.models import Restaurant

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

    class Meta:
        model = Restaurant
        fields = [
            'url',
            'user',
            'name',
            'location',
            'category',
        ]


class RestaurantRetrieveSerializer(ModelSerializer):
    delete_url = delete_url

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