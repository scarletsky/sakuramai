import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if not os.environ.get('APP_NAME', ''):
    MYSQL_DB = ''
    MYSQL_USER = ''
    MYSQL_PASS = ''
    MYSQL_HOST_M = ''
    MYSQL_HOST_S = ''
    MYSQL_PORT = ''
    DEBUG = True
    TEMPLATE_DEBUG = True
    MIDDLEWARE_CLASSES = (
        # 'django.middleware.cache.UpdateCacheMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        # 'django.middleware.cache.FetchFromCacheMiddleware',
    )

else:
    import sae.const
    MYSQL_DB = sae.const.MYSQL_DB
    MYSQL_USER = sae.const.MYSQL_USER
    MYSQL_PASS = sae.const.MYSQL_PASS
    MYSQL_HOST_M = sae.const.MYSQL_HOST
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S
    MYSQL_PORT = sae.const.MYSQL_PORT
    DEBUG = False
    TEMPLATE_DEBUG = False
    MIDDLEWARE_CLASSES = (
        # 'django.middleware.cache.UpdateCacheMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.gzip.GZipMiddleware',
        # 'django.middleware.cache.FetchFromCacheMiddleware',
    )


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.sinaapp.com',
]

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'white',
    'south',
)

# MIDDLEWARE_CLASSES = (
#     # 'django.middleware.cache.UpdateCacheMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.gzip.GZipMiddleware',
#     # 'django.middleware.cache.FetchFromCacheMiddleware',
# )

ROOT_URLCONF = 'sakuramai.urls'

WSGI_APPLICATION = 'sakuramai.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,
    }
}

# Cache
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}
# 12 hours
#CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 12

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

DUOSHUO_SECRET = ''
DUOSHUO_SHORT_NAME = ''
