# En custom_auth.py
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth = super().authenticate(request)

        if not auth:
            raise AuthenticationFailed('Authentication credentials were not provided.')

        return auth
