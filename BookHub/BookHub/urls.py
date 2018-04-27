from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from books import views
from books.views import BookHubApi
from comments.views import CommentViewSet
from accounts import urls as accounts_urls
from favourites.views import FavouriteViewSet
from users.views import UserViewSet


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = BookHubApi


api_router = DocumentedRouter()
api_router.register(r'books', views.BookViewSet)
api_router.register(r'authors', views.AuthorViewSet)
api_router.register(r'publishers', views.PublisherViewSet)
api_router.register(r'users', UserViewSet)


books_router = nested_routers.NestedSimpleRouter(api_router, r'books', lookup='books')
books_router.register(r'comments', CommentViewSet, base_name='book-comments')

users_router = nested_routers.NestedSimpleRouter(api_router, r'users', lookup='users')
users_router.register(r'favourites', FavouriteViewSet, base_name='user-favourites')

api_urlpatterns = [
    url('^', include(api_router.urls)),
    url('^', include(books_router.urls)),
    url('^', include(users_router.urls)),
]

urlpatterns = [
    path('accounts/', include(accounts_urls)),
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]
