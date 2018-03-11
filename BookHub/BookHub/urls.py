from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from books import views
from books.views import BookHubApi


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = BookHubApi


api_router = DocumentedRouter()
api_router.register(r'books', views.BookViewSet)
api_router.register(r'authors', views.AuthorViewSet)
api_router.register(r'publishers', views.PublisherViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
]
