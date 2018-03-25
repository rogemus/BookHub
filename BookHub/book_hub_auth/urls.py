from django.urls import path

from book_hub_auth.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='auth-login'),
]
