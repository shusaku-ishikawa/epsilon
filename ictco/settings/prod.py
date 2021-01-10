from .base import *

DEBUG = True

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'ictcodb',
    'USER': 'root',
    'PASSWORD': 'P@ssw0rd',
    'HOST': '127.0.0.1',
    'PORT': '3306',
  }
}