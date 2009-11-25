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
    
    'cnprog.middleware.pagesize.QuestionsPageSizeMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_authopenid.context_processors.authopenid',
    'cnprog.context_processors.auth_processor',
    'cnprog.context_processors.application_settings',
    )

ROOT_URLCONF = 'cnprog.urls'

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
    'cnprog',
    'cnprog_profile',
    'forum',
    #'debug_toolbar' ,
)


INTERNAL_IPS = ('127.0.0.1',)

#for OpenID auth
ugettext = lambda s: s
LOGIN_URL = '/accounts/signin'

#EMAIL AND ADMINS
ADMINS = (
    ('CNProg team', 'team@cnprog.com'),
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
APP_TITLE = u'CNProg.com 程序员问答社区'
APP_KEYWORDS = u'技术问答社区，中国程序员，编程技术社区，程序员社区，程序员论坛，程序员wiki，程序员博客'
APP_DESCRIPTION = u'中国程序员的编程技术问答社区。我们做专业的、可协作编辑的技术问答社区。'
APP_INTRO = u' <p>CNProg是一个<strong>面向程序员</strong>的可协作编辑的<strong>开放源代码问答社区</strong>。</p><p> 您可以在这里提问各类<strong>程序技术问题</strong> - 问题不分语言和平台。 同时也希望您对力所能及的问题，给予您的宝贵答案。</p>'
APP_COPYRIGHT = 'Copyright CNPROG.COM 2009'
 
GOOGLE_SITEMAP_CODE = '55uGNnQVJW8p1bbXeF/Xbh9I7nZBM/wLhRz6N/I1kkA='
GOOGLE_ANALYTICS_KEY = ''
EMAIL_VALIDATION = False

AUTH_PROFILE_MODULE = 'cnprog_profile.UserProfile'

# User settings
try:
    from local_settings import *
except ImportError:
    pass
