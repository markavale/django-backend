'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
DEBUG = True

WSGI_APPLICATION = 'base.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'frontend/public') ], # BASE_DIR / 'templates' depends on frontend => build
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

# DJANGO CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://127.0.0.1:3307",
    'http://localhost:3306'
]

CSRF_TRUSTED_ORIGINS = [
     "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "http://127.0.0.1:3307",
    'http://localhost:3306'
]
CORS_ALLOW_ALL_ORIGINS = True


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'PORT':config('PORT', cast=int),
#         'HOST':config('HOST'),
#         #'SSL':
#     }
# }

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://localhost:8081',
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]