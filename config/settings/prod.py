from .base import *

ALLOWED_HOSTS = ['34.64.118.189', 'www.dg1s.o-r.kr']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
MIDDLEWARE += ['django.middleware.clickjacking.XFrameOptionsMiddleware', ]
X_FRAME_OPTIONS = 'http://www.dg1s.o-r.kr/'
