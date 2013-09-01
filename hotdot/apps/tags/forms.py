# -*- coding: utf-8 -*-
from django import forms
from .models import Tag

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class TagAdminForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
