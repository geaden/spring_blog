# -*- coding: utf-8 -*-
from django.urls import path

from .views import PostsByTagView, AjaxTagsAutocomplete

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


urlpatterns = [
    path(r'^tag/(?P<pk>\d+)$', PostsByTagView.as_view(), name='detail'),
    path(r'^tags/autocomplete/$', AjaxTagsAutocomplete.as_view(), name='autocomplete'),
]