from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status

class CustomTokenVerifyView(TokenVerifyView):

    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('access_token');
        if not token:
            return Response({
                "message": "No access token provided in cookies"
            }, status.HTTP_400_BAD_REQUEST)
        
        try:
            UntypedToken(token)
            return Response(
                {"message": "Token is valid"}, status.HTTP_200_OK)
        except (InvalidToken, TokenError) as e:
            return Response(
                {"message": "Token is invalid or expired.", 'error': str(e)},
                status.HTTP_401_UNAUTHORIZED
            )