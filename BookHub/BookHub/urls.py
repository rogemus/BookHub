from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from books import views
from books.views import BookHubApi
from comments.views import CommentViewSet


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = BookHubApi


api_router = DocumentedRouter()
api_router.register(r'books', views.BookViewSet)
api_router.register(r'authors', views.AuthorViewSet)
api_router.register(r'publishers', views.PublisherViewSet)

domains_router = nested_routers.NestedSimpleRouter(api_router, r'books', lookup='books')
domains_router.register(r'comments', CommentViewSet, base_name='book-comments')

api_urlpatterns = [
    url('^', include(api_router.urls)),
    url('^', include(domains_router.urls)),
]

urlpatterns = [
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]
