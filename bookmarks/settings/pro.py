from .base import *


DEBUG = False

THUMBNAIL_DEBUG = False

ADMIN = (
    ('polar9527', 'polar9527@163.com'),
)

ALLOWED_HOSTS = []

with open(os.path.join(BASE_DIR, 'mysql.passwd')) as f:
    mysqlpwd = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookmarks',
        'USER': 'bookmarks',
        'PASSWORD': mysqlpwd,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}