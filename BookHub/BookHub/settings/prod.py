from .base import *  # noqa

ALLOWED_HOSTS = ['api.bookhub.com']
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '/static'))

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
