### -*- coding: utf-8 -*- ##

import os.path

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from forum.models import Question

urlpatterns = patterns('',
    url(r'^$', 'forum.views.questions', 
        {'queryset': Question.objects.all()}, 
        name='questions'),
    url(r'^unanswered/$', 'forum.views.questions', 
        {'template_name': 'unanswered.html',
         'queryset': Question.objects.filter(answer_count=0),
         'extra_context': {'is_unanswered':True},
         }, name='unanswered'),
)