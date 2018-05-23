"""
Django settings for nucleus project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import normpath, join

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ghobvfrewhrxxlxl&((#kbx7bsc8+*fepe@k=qf+p01$^fi*qp'

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
    'django.contrib.staticfiles', # This brings the static files together.
    # Added entry for blog app - AKSHAY GAUR
    'blog',
    # Added entry for class management app - AKSHAY GAUR
    'class_management',
    # Added entry for documentation of the app - AKSHAY GAUR
    'django.contrib.admindocs',
    # Added entry for widget-tweaks for that sweet sweet form display
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nucleus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Added DIRS for being able to access base.html from outside the app folder.
        'DIRS': [
            normpath(join(BASE_DIR, 'templates')),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Added context processor for MEDIA_URL in templates.
                'django.template.context_processors.media',
            ],
            # Added builtins(as of 1.9) so that static context need not be loaded for every template.
            # If this doesn't work then {% load static %} will need to be put in every html file.
            'builtins':[
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]

WSGI_APPLICATION = 'nucleus.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tutorial_database',
        'USER': 'tutorial_user',
        'PASSWORD': 'tutorial',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Changed timezone - AKSHAY GAUR
TIME_ZONE = 'US/Central'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Added static root - AKSHAY GAUR
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'storage', 'static')


# Added img root and url.
# MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/img')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'storage', 'media')
MEDIA_URL = '/assets/'

# STATICFILES_DIRS for serving js, css stuff
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
