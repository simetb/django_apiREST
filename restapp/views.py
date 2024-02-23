from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from .custom_auth import CustomTokenAuthentication
from django.http import JsonResponse
from rest_framework.views import APIView


class CSRFTokenView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        csrf_token = request.META.get('HTTP_X_CSRFTOKEN', '')
        if csrf_token:
            return JsonResponse({'message': 'Hello', 'csrf_token': csrf_token})
        else:
            return JsonResponse({'error': 'CSRF token was not provided in the request header'}, status=400)

class HelloWorldView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        csrf_token = request.META.get('CSRF_COOKIE', '')

        if request.user.is_authenticated:
            return Response({'message': 'Hola mundo', 'csrf_token': csrf_token})
        else:
            return Response({'error': 'Authentication credentials were not provided.'}, status=401)

class LoginView(APIView):
    
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)