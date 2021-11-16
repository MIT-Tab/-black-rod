"""
Django settings for apda project.

Generated by 'django-admin startproject' using Django 1.11.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3j$y%c@9o%b-1mf$n=$bps=qvt^ls!l_5juf+%1_&w46t$1-q*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
BASE_URL = 'http://50.116.54.146'


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    'webpack_loader',
    'menu_generator',
    'crispy_forms',
    'import_export',
    'django_tables2',
    'formtools',
    'haystack',
    'taggit',
    'django_summernote',

    'core',
    'django_extensions',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',    
    'apdaonline',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apda.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'apda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

SEASONS = (
    ('2020', '2020-21'),
    ('2019', '2019-20'),
    ('2018', '2018-19'),
    ('2017', '2017-18'),
    ('2016', '2016-17'),
    ('2015', '2015-16'),
    ('2014', '2014-15'),
    ('2013', '2013-14'),
    ('2012', '2012-13'),
    ('2011', '2011-12'),
    ('2010', '2010-11'),
    ('2009', '2009-10'),        
    ('2008', '2008-09'),
    ('2007', '2007-08'),
    ('2006', '2006-07'),
    ('2005', '2005-06'),
    #('2004', '2004-05'),
    #('2003', '2003-04'),
)

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

DEFAULT_SEASON = '2020'
CURRENT_SEASON = '2020'
QUAL_BAR = 16.5

ONLINE_SEASONS = (
    '2020',
)
ONLINE_QUAL_BAR = 10

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'webpack_bundles/', # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'

SOCIALACCOUNT_ADAPTER = 'apdaonline.adapter.APDAOnlineAdapter'
SOCIALACCOUNT_PROVIDERS = {
    'apdaonline': {
        'APP': {
            'client_id': 'trFRQPwEPoARBgpFaGGz2FunZ5IAYuMtH9xFjcCI',
            'secret': 'gZmR7Fz1cPDlJZG4XYJM1XdwFRjFmztQM55BZSVd',
            'key': ''
        }
    }
}

SITE_ID = 1

NAV_MENU_LEFT = [
    {
        'name': 'Standings',
        'url': 'core:index'
    },
    {
        'name': 'Results',
        'validators': ['menu_generator.validators.is_authenticated'],
        'url': '/asdfa',
        'submenu': [
            {
                'name': 'Schools',
                'url': 'core:school_list',
                'root': True
            },
            {
                'name': 'Debaters',
                'url': 'core:debater_list',
                'root': True
            },
            {
                'name': 'Tournaments',
                'url': 'core:tournament_list',
                'root': True
            },
            {
                'name': 'Teams',
                'url': 'core:team_list',
                'root': True
            },            
        ]
    },
    {
        'name': 'Videos',
        'url': 'core:video_list',
        'root': True
    },
    {
        'name': 'Results',
        'validators': ['menu_generator.validators.is_anonymous'],
        'url': 'core:tournament_list',
        'root': True
    },
    {
        'name': 'Schedule',
        'url': 'core:schedule_view',
        'root': True
    },
    {
        'name': 'Admin',
        'url': '/admin/',
        'validators': ['menu_generator.validators.is_superuser']
    },
    {
        'name': 'Feedback',
        'url': 'https://forms.gle/b5P8mU8inAerZVY58'
    },
    {
        'name': 'apda.online',
        'url': 'http://apda.online',
    },
    {
        'name': 'Login',
        'url': '/auth/login/',
        'validators': ['menu_generator.validators.is_anonymous']
    },
    {
        'name': 'Logout',
        'url': '/auth/logout/',
        'validators': ['menu_generator.validators.is_authenticated']
    }
]

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

DJANGO_TABLES2_TEMPLATE = 'base/table.html'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

SUMMERNOTE_THEME = 'lite'


SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
    }
}
