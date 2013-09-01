# -*- coding: utf-8 -*-
from django.template import Context, Template
from django.test import TestCase
from django.conf import settings


from ...tags.models import Tag


__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class BlogExtrasTestCase(TestCase):
    def render_template(self, template, context):
        context = Context(context)
        return Template(template).render(context)

    def test_pagebreak(self):
        content = '<p>foo</p>' + settings.SEPARATOR + '<p>bar</p>'
        rendered = self.render_template(
            "{% load blog_extras %}"
            "{{ content|safe|pagebreak }}",
            {
                "content": content
            }
        )
        self.assertNotIn('<p>bar</p>', rendered)

    def test_taglink(self):
        Tag.objects.create(name='foo')
        Tag.objects.create(name='bar')
        rendered = self.render_template(
            "{% load blog_extras %}"
            "{{ tags|taglink|join:', ' }}",
            {'tags': Tag.objects.all}
        )
        self.assertEquals(2, rendered.count('<a'))
