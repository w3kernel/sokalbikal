"""
Django settings for sokalbikall project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
from .mail_info import *

# Mail information
# EMAIL_HOST = EMAIL_HOST
# EMAIL_HOST_USER = EMAIL_HOST_USER  # SET EMAIL
# EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD  # SET PASSWORD OR APP PASSWORD
# EMAIL_PORT = EMAIL_PORT
# EMAIL_USE_SSL = EMAIL_USE_SSL
DEFAULT_FROM_EMAIL = 'Sokalbikal'
BASE_URL = '127.0.0.1:8000'  # SET YOUR BASE URL [BASE_URL = '127.0.0.1:8000']

MANAGERS = [
    ('Shamsul Haq', 'shamsulcitycse@gmail.com'),  # Just like ('khan', 'khan@gmail.com')
]

ADMINS = MANAGERS
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z+xy!5-b%=)9dev$chum#k8odpd)6g9cm-%-4+baghe$1ltb94'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]
THIRD_PARTY_APPS = [
    'widget_tweaks',
    'mptt',
    'image_optimizer',
    'crispy_forms',
]

LOCAL_APPS = [
    'accounts',
    'product',
    'vendor',
    'customer',
    'cart',
    'ordermanager',
    'core',
]

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS
# Custom User Auth
AUTH_USER_MODEL = 'accounts.User'

# Login and Logout
LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOGOUT_URL = '/logout/'
LOGOUT_URL_REDIRECT = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sokalbikall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'sokalbikall.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# # Add MYSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sokalbikal',
#         'USER': 'root',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Message framework
MESSAGE_TAGS = {
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
    messages.WARNING: 'alert alert-warning',
    messages.ERROR: 'alert alert-danger',
    messages.DEBUG: 'alert alert-info',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Cart Session ID
CART_SESSION_ID = 'cart'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = "/static/"

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
OPTIMIZED_IMAGE_METHOD = 'pillow'