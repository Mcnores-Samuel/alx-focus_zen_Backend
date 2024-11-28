"""This module contains a custom token refresh class to ensure access security"""
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenRefreshView(TokenObtainPairView):
    """Custome token refresh access point"""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data


        response.set_cookie(
            key='access_token',
            value=data['access'],
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=300
        )
        del data['access']

        return response