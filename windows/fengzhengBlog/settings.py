"""
Django settings for fengzhengBlog project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9h94=&s3bk!5+6b(-d^(62%_7-4r89f8pm6*4h15d85yi=ww=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

import fengzhengBlog.blogapp
# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fengzhengBlog.blogapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fengzhengBlog.urls'

WSGI_APPLICATION = 'fengzhengBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"mypythonblog",
        'USER': 'USERNAME',                      # 
        'PASSWORD': 'PASSWORD',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'zh-cn' #en-us

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS=(
    #"F:/PythonDjangoWeb/fengzhengBlog/fengzhengBlog/template",
    #os.path.join(os.path.dirname(__file__), '/template').replace('\\','/'),
    (os.path.dirname(__file__)+"/template").replace('\\','/'),
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(name)s %(asctime)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(name)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_request':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s status_code:%(status_code)d',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'django_db_backends':{
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(lineno)d %(message)s duration:%(duration).3f sql:%(sql)s params:%(params)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'custom_log_file':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'verbose'
        },
        'django_request_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_request_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_request'
        },
        'django_db_backends_logfile':{
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django_db_backends_logfile.log'),#you need define your VAR_ROOT variable that points to your project path,and mkdir a logs directory in your project root path.
            'backupCount': 5,
            'maxBytes': '16777216', # 16megabytes(16M)
            'formatter': 'django_db_backends'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins','django_request_logfile'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['django_db_backends_logfile',],
            'level': 'WARNING',
            'propagate': True,
        },
        'customapp': {#then you can change the level to control your custom app whether to output the debug infomation
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'customapp.engine': {#then you can change the level to control your custom app whether to output the debug infomation
            'handlers': ['custom_log_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}