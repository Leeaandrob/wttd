# coding: utf-8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.core.views',
    url(r'^$', 'homepage', name='homepage'),
    url(r'^dir/index.html$', 'index_alexandre', name='index_alexandre'),
)