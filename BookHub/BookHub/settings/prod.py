from .base import *  # noqa


ALLOWED_HOSTS = ['bookhub.com']

STATIC_ROOT = os.environ.get('STATIC_ROOT', '/static')


# SSL/ HTTPS Configs

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
