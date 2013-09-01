# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models

from .models import Tag
from .forms import TagAdminForm

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_posts')
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

    def has_add_permission(self, request):
        return False

    class Meta:
        form = TagAdminForm


admin.site.register(Tag, TagAdmin)