from django.urls import path
from rest_framework import routers

from accounts.views import LoginView, RegisterView

router = routers.SimpleRouter()
router.register(r'register', RegisterView, base_name='register')

urlpatterns = [
    path('login/', LoginView.as_view()),
]

urlpatterns += router.urls
