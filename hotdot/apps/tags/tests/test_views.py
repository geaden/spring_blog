# -*- coding: utf-8 -*-
import json
from django.urls import reverse
from django.test import TestCase

from ..models import Tag
from ...blog.models import Post

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class TagsViewsTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name='foo')
        # create 11 posts with this tag
        for i in range(11):
            post = Post.objects.create(title='foo',
                                       content='bar')
            post.tags.add(self.tag)
            post.save()
        self.tag_url = reverse('tag:detail', args=[self.tag.pk])

    def test_posts_by_tags_view(self):
        response = self.client.get(self.tag_url)

        self.assertEquals(200, response.status_code)

        self.assertEquals(len(response.context['posts_list']),
                          10)

        # test pagination
        self.assertIn('pager', response.content)

        response = self.client.get(self.tag_url + '?page=2')

        self.assertEquals(200, response.status_code)

        self.assertEquals(len(response.context['posts_list']),
                          1)

    def test_tags_autocomplete(self):
        Tag.objects.create(name='foo1')
        Tag.objects.create(name='foo2')
        autocomplete_url = reverse('tag:autocomplete')
        query = '?term=%s'
        url = autocomplete_url + query % 'foo'
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        data = json.loads(response.content)
        self.assertEquals(3, len(data))
        url = autocomplete_url + query % 'foo1'
        response = self.client.get(url)
        self.assertEquals(200, response.status_code)
        data = json.loads(response.content)
        self.assertEquals(1, len(data))




