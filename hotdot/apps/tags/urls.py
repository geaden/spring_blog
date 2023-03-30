# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import PostsByTagView, AjaxTagsAutocomplete

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


urlpatterns = [
    re_path(r'^tag/(?P<pk>\d+)$', PostsByTagView.as_view(), name='detail'),
    re_path(r'^tags/autocomplete/$', AjaxTagsAutocomplete.as_view(), name='autocomplete'),
]