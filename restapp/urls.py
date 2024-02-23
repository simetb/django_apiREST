from django.urls import path
from .views import CSRFTokenView, LoginView, HelloWorldView

urlpatterns = [
    path('test/',CSRFTokenView.as_view(), name='test'),
    path('login/',LoginView.as_view(), name='login'),
    path('helloworld/',HelloWorldView.as_view(), name='helloworld'),
]