### -*- coding: utf-8 -*- ####################################################

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '1.0'

install_requires = [
    'setuptools==0.6c11',
    'Django==1.1.1',
    'markdown2==1.0.1.16',
    'python-openid==2.2.4',
    'html5lib==0.11.1',
    'django-extensions==0.4.1',

    'app_media',
    'django_authopenid',
    'django-profiles',
]

extras_require = dict(
    test = ['coverage==3.2',
            'windmill==1.3',
            ]
)

#AFAIK:
install_requires.extend(extras_require['test'])

setup(
    name = "qna",
    version = version,
    description = "Q&A System",
    long_description = read('README'),
    author = 'Chen Gang',
    url = 'http://answerlog.net.com',
    maintainer="Answerlog",
    maintainer_email="admin@answerlog.net",
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires = install_requires,
    extras_require = extras_require,
    entry_points="""
      # -*- Entry points: -*-
      """,
)
