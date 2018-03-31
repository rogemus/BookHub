from .base import *  # noqa

ALLOWED_HOSTS = ['book-hub.com', 'localhost', '127.0.0.1']
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '/static'))
