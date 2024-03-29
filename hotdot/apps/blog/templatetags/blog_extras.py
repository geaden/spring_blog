# -*- coding: utf-8 -*-
import logging
from django import template
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from ...tags.models import Tag


__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def pagebreak(value):
    """
    Page break for post on main page
    """
    sep = value.find(settings.SEPARATOR)
    if sep != -1:
        value = value[:sep]
    return value


@register.filter()
def taglink(value):
    """
    Generates tag link
    """
    result = []
    for tag_name in value:
        try:
            tag = Tag.objects.get(name=tag_name)
        except Tag.DoesNotExist:
            logging.warning('Tag with name %s not found', tag_name)
            tag = None
        if tag:
            url = reverse('tag:detail', args=[tag.pk,])
            link = mark_safe('<a href="{url}">{name}</a>'.format(
                url=url, name=tag.name))
            result.append(link)
    return result
