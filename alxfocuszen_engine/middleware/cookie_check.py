from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed


def jwt_cookie_authentication(get_response):
    def middleware(request):
        access_token = request.COOKIES.get('access_token')
        if access_token:
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(access_token)
                user = jwt_auth.get_user(validated_token)
                request.user = user
            except AuthenticationFailed:
                pass
        return get_response(request)
    
    return middleware