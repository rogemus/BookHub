from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from books import views

api_router = routers.DefaultRouter()
api_router.register(r'books', views.UserViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
]
