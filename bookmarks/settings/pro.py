from .base import *


DEBUG = False

THUMBNAIL_DEBUG = False

ADMIN = (
    ('polar9527', 'polar9527@163.com'),
)

#ALLOWED_HOSTS = ['www.bookmarks.com', '127.0.0.1']
ALLOWED_HOSTS = ['ec2-52-78-179-108.ap-northeast-2.compute.amazonaws.com','127.0.0.1', 'localhost',]

with open(os.path.join(BASE_DIR, 'mysql.passwd')) as f:
    mysqlpwd = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookmarksdb',
        'USER': 'bookmarks',
        'PASSWORD': mysqlpwd,
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
