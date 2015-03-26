"""
Django settings for placementCell project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import dirname,join
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2@chy=a&sh5wu%&0%h0c&aa@tf%qx1w6yd7#p4o*re+-fx=jj#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tpc',
    'tastypie',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

PUSH_NOTIFICATIONS_SETTINGS={
"GCM_API_KEY":"AIzaSyBlOoPcqND433n7B5Nu22ZzaqGc_bAXV2Q",
"GCM_POST_URL":"https://android.googleapis.com/gcm/send"
}

ROOT_URLCONF = 'placementCell.urls'

WSGI_APPLICATION = 'placementCell.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


import dj_database_url

DATABASES = { 'default' : dj_database_url.config()}
'''
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
	'NAME': 'placement',
	'USER':'root',
	'PASSWORD':'mysql',
	'HOST':'localhost',
	'PORT':'3306',
    }
}'''	
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True

API_LIMIT_PER_PAGE = 0


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= 'staticfiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT=join(BASE_DIR,'media')
MEDIA_URL='/media/'
