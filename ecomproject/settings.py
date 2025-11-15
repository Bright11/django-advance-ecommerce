

from pathlib import Path
import paypalrestsdk
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$i=%9ph1&_egctk$-9-dp=jnng6n203=egv+zb+#t18^^eeds6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# login
LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/'
#LOGOUT_REDIRECT_URL='/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'commapp',
    'adminapp',
    'authapp',
    'paypalapp'
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

ROOT_URLCONF = 'ecomproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'commapp.context_processors.category',
                'adminapp.analaystics.analaytics',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL='media/'
MEDIA_ROOT= BASE_DIR/'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

paypalrestsdk.configure({
    "mode": "sandbox", # sandbox or live
    "client_id": "AXN4F1LIDIA8dA13G90LvZgedpkAp7HJRoWMvrCNnQgCU3MUMc1LnN0MR9iMaIGBwC2xCkegV2uhYGHE",
    "client_secret": "EOiYXId7daCuGOF5tXbcIbhTFfE3vbqkd6sP8TNbQC3I5JJTmUU3QbE07vVXPdCXBzuE_O4khx5RXBrN",
    'PAYPAL_MODE': 'sandbox' 
})

PAYPAL_CLIENT_ID='AXN4F1LIDIA8dA13G90LvZgedpkAp7HJRoWMvrCNnQgCU3MUMc1LnN0MR9iMaIGBwC2xCkegV2uhYGHE'

PAYPAL_CLIENT_SECRET='EOiYXId7daCuGOF5tXbcIbhTFfE3vbqkd6sP8TNbQC3I5JJTmUU3QbE07vVXPdCXBzuE_O4khx5RXBrN'
PAYPAL_MODE = 'sandbox' 