# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PostsByTagView, AjaxTagsAutocomplete

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


urlpatterns = patterns(
    '',
    url(r'^tag/(?P<pk>\d+)$', PostsByTagView.as_view(), name='detail'),
    url(r'^tags/autocomplete/$', AjaxTagsAutocomplete.as_view(), name='autocomplete'),

    )