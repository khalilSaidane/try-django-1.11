from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from profiles.models import Profile


class ProfileFollowAPIToggle(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,username=None, format=None):
        is_following, profile_ = Profile.objects.toggle_follow(request.user, username)
        data = {
            "is_following": is_following,
            "profile_": profile_.user.username
        }
        return Response(data)
