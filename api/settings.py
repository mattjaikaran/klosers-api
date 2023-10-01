"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
import dj_database_url


ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
print(f">>> #ENVIRONMENT: {ENVIRONMENT} <<<")
IN_DEV = ENVIRONMENT == "development"
IN_STAGING = ENVIRONMENT == "staging"
IN_PROD = ENVIRONMENT == "production"


def _env_get_required(setting_name):
    """Get the value of an environment and assert that it is set"""
    setting = os.environ.get(setting_name, "")
    if IN_STAGING or IN_PROD:
        assert setting not in {
            None,
            "",
        }, "{0} must be defined as an environment variable.".format(setting_name)
    return setting


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _env_get_required("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _env_get_required("DEBUG")

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "corsheaders",
    "django.contrib.sites",
    # authentication
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # app
    "common",
    "core",
    "sales",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("GOOGLE_CLIENT_ID"),
            "secret": os.environ.get("GOOGLE_CLIENT_SECRET"),
            "key": "",  # leave empty
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {"access_type": "online"},
        "VERIFIED_EMAIL": True,
    }
}

ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "allauth.account.middleware.AccountMiddleware",
]


ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"
ASGI_APPLICATION = "api.asgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

heroku_default_db = dj_database_url.config()

if bool(heroku_default_db):
    DATABASES = {"default": heroku_default_db}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": _env_get_required("DATABASE_NAME"),
            "USER": _env_get_required("DATABASE_USER"),
            "PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
            "HOST": _env_get_required("DATABASE_HOST"),
            "PORT": _env_get_required("DATABASE_PORT"),
        }
    }

REST_AUTH = {
    "LOGIN_SERIALIZER": "dj_rest_auth.serializers.LoginSerializer",
    "TOKEN_SERIALIZER": "dj_rest_auth.serializers.TokenSerializer",
    "JWT_SERIALIZER": "dj_rest_auth.serializers.JWTSerializer",
    "JWT_SERIALIZER_WITH_EXPIRATION": "dj_rest_auth.serializers.JWTSerializerWithExpiration",
    "JWT_TOKEN_CLAIMS_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "USER_DETAILS_SERIALIZER": "dj_rest_auth.serializers.UserDetailsSerializer",
    "PASSWORD_RESET_SERIALIZER": "dj_rest_auth.serializers.PasswordResetSerializer",
    "PASSWORD_RESET_CONFIRM_SERIALIZER": "dj_rest_auth.serializers.PasswordResetConfirmSerializer",
    "PASSWORD_CHANGE_SERIALIZER": "dj_rest_auth.serializers.PasswordChangeSerializer",
    "REGISTER_SERIALIZER": "dj_rest_auth.registration.serializers.RegisterSerializer",
    "REGISTER_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "TOKEN_MODEL": "rest_framework.authtoken.models.Token",
    "TOKEN_CREATOR": "dj_rest_auth.utils.default_create_token",
    "PASSWORD_RESET_USE_SITES_DOMAIN": False,
    "OLD_PASSWORD_FIELD_ENABLED": False,
    "LOGOUT_ON_PASSWORD_CHANGE": False,
    "SESSION_LOGIN": True,
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "kloser-cookie-auth",
    "JWT_AUTH_REFRESH_COOKIE": "my-refresh-token2822",
    "JWT_AUTH_REFRESH_COOKIE_PATH": "/",
    "JWT_AUTH_SECURE": False,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_SAMESITE": "Lax",
    "JWT_AUTH_RETURN_EXPIRATION": False,
    "JWT_AUTH_COOKIE_USE_CSRF": False,
    "JWT_AUTH_COOKIE_ENFORCE_CSRF_ON_UNAUTHENTICATED": False,
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1  # Needed for allauth
REST_USE_JWT = True  # to use JSON web tokens

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "id",
    "SIGNING_KEY": os.environ.get("JWT_SECRET_KEY"),
    "ALGORITHM": "HS512",
}

REST_AUTH_SERIALIZERS = {"USER_DETAILS_SERIALIZER": "core.CustomUserSerializer"}

# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "allauth.account.auth_backends.AuthenticationBackend",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "core.CustomUser"
# LOGIN_URL = "/auth/login"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "static/"

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# STATIC

FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240


ADMIN_URL = "admin/"
ADMINS = [("""Klosers""", "mattjaikaran@gmail.com")]
MANAGERS = ADMINS
