from django.urls import path

from accounts.views import login_view as LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView, name='account-login'),
    path('register/', RegisterView, name='account-register'),
]
