from django.urls import path

from accounts.views import LoginView, AboutUserView, Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', AboutUserView.as_view(), name='me'),
]
