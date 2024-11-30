from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone


class CustomTokenObtainPairView(TokenObtainPairView):
    """This is a custom token authentication access point to allow 
    secure storage of the access token
    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Sets access token and refresh token as cookies, allowing zero access token
        being exposed.
        """
        response = super().post(request, *args, **kwargs)
        data = response.data


        response.set_cookie(
            key='access_token',
            value=data['access'],
            httponly=True,
            secure=True,
            samesite='Strict',
            max_age=timezone.timedelta(minutes=60).total_seconds()
        )
        response.set_cookie(
            key='refresh_token',
            value=data['refresh'],
            httponly=True,
            secure=True,
            samesite='Strict',
            max_age=timezone.timedelta(days=7).total_seconds()
        )

        del data['access']
        del data['refresh']

        return response
