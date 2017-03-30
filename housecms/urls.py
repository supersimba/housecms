#coding:utf-8

from django.conf.urls import url
from django.views.generic.base import TemplateView
from django.contrib import admin

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #
    url(r'^mgrindex',TemplateView.as_view(template_name='cmsapp/mgrindex.html')),
    url(r'^mgrhouse',TemplateView.as_view(template_name='cmsapp/mgrhouse.html')),
    url(r'^addhouse',TemplateView.as_view(template_name='cmsapp/addhouse.html')),
]
