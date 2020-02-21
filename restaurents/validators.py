from django.core.exceptions import ValidationError


def validate_name(value):
    if value == 'Tacos':
        raise ValidationError(
            'We dont like tacos here !!!',
            params={'value': value},
        )

