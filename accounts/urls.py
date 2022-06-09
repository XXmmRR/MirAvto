from django.urls import path
from .views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
    ]
