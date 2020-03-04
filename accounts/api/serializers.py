from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    EmailField
)
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email2 = EmailField(label='Confirm email')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2'
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get('email')
        email2 = value
        if email != email2:
            raise ValidationError('Emails do not match.')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('User already registered.')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
