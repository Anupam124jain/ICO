"""
Django settings for ico project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yzl0@opw!f1u+!k+-gk+f098q)8vgf10(dc^a+bacud^)oy17v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Site ID
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'webapp.apps.WebappConfig',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.py_solc.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # <--
]

ROOT_URLCONF = 'ico.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'webapp/templates'),
            os.path.join(BASE_DIR, 'main/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ico.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ico',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    'main.backend.EmailBacked',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
)
LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_TWITTER_KEY = 'anvmffrNYY8EqhUV7efPWHV9M'
SOCIAL_AUTH_TWITTER_SECRET = 'BwsA38C2DchDdJqgZZ8dQmSzKbulT1E4tZCu8rjNPK2JFLnDp1'


SOCIAL_AUTH_FACEBOOK_KEY = '1108115082698211'
SOCIAL_AUTH_FACEBOOK_SECRET = 'dfa8132d55684943d69866849ade66c3'
# Only works when HTTPS : fb new policy
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media File's settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SOLIDITY_DIR = os.path.join(BASE_DIR, 'webapp/py_solc')


EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'testing@purpose.com'
SERVER_EMAIL = 'magento@ranosys.net'
EMAIL_HOST = 'mail.ranosys.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'magento@ranosys.net'
EMAIL_HOST_PASSWORD = 'U#Y4-JC5JG(M'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
