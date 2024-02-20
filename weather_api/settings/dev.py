from .common import *

SECRET_KEY = 'django-insecure-1+^re1g(0t3xh&==-cs%kg2fx(81&4$jxqcyn#ffpv627gv@*t'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
