'''Use this for production'''
import os
import dj_database_url
from .base import *

DEBUG = False
SECRET_KEY = config('SECRET_KEY')#
ALLOWED_HOSTS += ['http://domain.com'] # PUT HERE YOUR DOMAIN NAME WHEN YOU DEPLOY YOUR WEB APP

WSGI_APPLICATION = 'base.wsgi.prod.application'

############
# DATABASE #
############
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}
CORS_ALLOWED_ORIGINS = [
    'https://markanthonyvale.herokuapp.com',
    'https://admin-mav.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com',
    # 'http://markanthonyvale.herokuapp.com'
]

CSRF_TRUSTED_ORIGINS = [
    'https://admin-scraper.herokuapp.com',
    #'https://markanthonyvale.herokuapp.com', # 
    #'https://admin-mav.herokuapp.com', # 
]
CORS_ALLOW_ALL_ORIGINS = False
CORS_ORIGIN_WHITELIST = [
    'https://admin-scraper.herokuapp.com',
] 


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'dist' ], # BASE_DIR / 'templates' depends on frontend => build
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATIC_URL = '/static/'
# Place static in the same location as webpack build files
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'dist/static'
    ]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# CSRF_COOKIE_SECURE = True
# http conf
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

'''
    ENV VARIABLES SECTION
'''
TESTING = False