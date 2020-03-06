from django.db.models.signals import post_save
from profiles.models import Profile
from restaurents.models import Restaurant
from django.conf import settings
User = settings.AUTH_USER_MODEL


def notify_on_follow(sender, instance, *args, **kwargs):
    pass
