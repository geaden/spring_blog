# -*- coding: utf-8 -*-
from functools import partial
from django.contrib.admin.utils import flatten_fieldsets
from django.contrib.contenttypes.models import ContentType

from django.urls import reverse
from django.contrib import admin
from django.forms.models import modelform_factory

from .models import Post
from .forms import PostAdminForm
from ..tags.models import Tag
from tinymce.widgets import TinyMCE

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_draft',)
    date_hierarchy = 'created'
    form = PostAdminForm
    search_fields = ('title',)
    list_filter = ('is_draft', 'pub_date')
    list_per_page = 10
    ordering = ('-pub_date',)

    class Media:
        js = (
            'js/jquery-1.10.2.min.js',
            'js/jquery-ui-1.10.3.custom.min.js',
            'tinymce/tinymce.min.js',
            'js/jquery.tagsinput.min.js',
            'js/tags.js')
        css = {'all': ('css/jquery.tagsinput.css',
                       'css/jquery-ui-1.10.3.custom.min.css',
                       'css/tags.css')}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 50, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def save_form(self, request, form, change):
        post = form.save(commit=False)
        post.save()
        tag_names = form.cleaned_data['tags'].split(',')
        if change:
            post.tags.clear()
        if tag_names:
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
            post.save()
        form.save_m2m()
        return super(PostAdmin, self).save_form(request, form, change)



admin.site.register(Post, PostAdmin)