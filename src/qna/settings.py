# encoding:utf-8
# Django settings for lanai project.
import os.path
from django.conf import global_settings
#DEBUG SETTINGS
DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'site_media')
APP_MEDIA_ROOT = MEDIA_ROOT

SERVE_MEDIA = True

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin/media/'
SECRET_KEY = '$oo^&_m&qwbib=(_4m_n*zn-d=g#s0he5fx9xonnym#8p6yigm'
# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (   
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    
    'qna.middleware.pagesize.QuestionsPageSizeMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_authopenid.context_processors.authopenid',
    'qna.context_processors.auth_processor',
    'qna.context_processors.application_settings',
    )

ROOT_URLCONF = 'qna.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django_extensions',
    'profiles',
    'django_authopenid',
    'app_media',
    'qna',
    'qna_profile',
    'forum',
    #'debug_toolbar' ,
)


INTERNAL_IPS = ('127.0.0.1',)

#for OpenID auth
ugettext = lambda s: s
LOGIN_URL = '/accounts/signin'

#EMAIL AND ADMINS
ADMINS = (
    ('CNProg team', 'team@qna.com'),
)
MANAGERS = ADMINS


#UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = os.path.join(os.path.dirname(__file__), 'tmp').replace('\\','/')
FILE_UPLOAD_HANDLERS = ("django.core.files.uploadhandler.MemoryFileUploadHandler",
 "django.core.files.uploadhandler.TemporaryFileUploadHandler",)
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
# for user upload
ALLOW_FILE_TYPES = ('.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tiff')
# unit byte
ALLOW_MAX_FILE_SIZE = 1024 * 1024

#OTHER SETTINGS
APP_TITLE = ''
APP_KEYWORDS = ''
APP_DESCRIPTION = ''
APP_INTRO = ''
APP_COPYRIGHT = ''
APP_URL = 'http://example.com:8001'
 
GOOGLE_SITEMAP_CODE = ''
GOOGLE_ANALYTICS_KEY = ''
EMAIL_VALIDATION = False

AUTH_PROFILE_MODULE = 'qna_profile.UserProfile'

# Templatesadmin
# Settings for templates editing via django admin
 
TEMPLATESADMIN_HIDE_READONLY = True
TEMPLATESADMIN_GROUP = 'Editors'
TEMPLATESADMIN_VALID_FILE_EXTENSIONS = (
        'html',
        'css',
        'txt',
        'backup',
   )
 
TEMPLATESADMIN_EDITHOOKS = (
         'templatesadmin.edithooks.dotbackupfiles.DotBackupFilesHook',
   )

# User settings
try:
    from local_settings import *
except ImportError:
    pass
