# -*- coding: utf-8 -*-
from copy import deepcopy
import json
from django import http
from django.core.paginator import Paginator, PageNotAnInteger

from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Tag
from ..blog.models import Post

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class PostsByTagView(DetailView):
    model = Tag

    def get_context_data(self, **kwargs):
        ctx = super(PostsByTagView, self).get_context_data(**kwargs)
        posts = Post.objects.filter(
            tags__name__exact=self.get_object().name)
        paginator = Paginator(posts, 10)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        ctx['posts_list'] = posts
        return ctx


class AjaxTagsAutocomplete(ListView):
    model = Tag
    context_object_name = 'tags_list'

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse(json.dumps([tag.name for tag in self.get_queryset()]),
                            content_type='application/json',
                            **response_kwargs)

    def get_queryset(self):
        queryset = super(AjaxTagsAutocomplete, self).get_queryset()
        if self.request.GET.has_key('term'):
            queryset = self.model.objects.filter(
                name__istartswith=self.request.GET['term'])[:10]
        return queryset