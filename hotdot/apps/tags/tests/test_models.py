# -*- coding: utf-8 -*-
from django.test import TestCase

from ..models import Tag

from ...blog.models import Post


__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class TagModelTestCase(TestCase):
    def test_tag_create(self):
        Tag.objects.create(name='foo')
        self.assertEquals(1, Tag.objects.all().count(),
                          msg='Number of tags should be one')

    def test_tag_edit(self):
        Tag.objects.create(name='foo')
        tag = Tag.objects.get(name='foo')
        tag.name = 'bar'
        tag.save()
        updated_tag = Tag.objects.all()[0]
        self.assertEquals('bar', updated_tag.name,
                          msg='Tag name should be `bar`')

    def test_tag_delete(self):
        Tag.objects.create(name='foo')
        before = Tag.objects.all().count()
        tag = Tag.objects.get(name='foo')
        tag.delete()
        after = Tag.objects.all().count()
        self.assertEquals(before - 1, after,
                          msg='Number of tags should be less by one')

    def test_get_post_by_tag(self):
        tag1 = Tag.objects.create(name='foo')
        post1 = Post.objects.create(title='foo', content='bar')
        post1.tags.add(tag1)
        tag2 = Tag.objects.create(name='bar')
        post2 = Post.objects.create(title='bar', content='buz')
        post2.tags.add(tag2)
        posts = tag1.posts.all()
        self.assertEquals(1, posts.count(), msg='Number of posts should be 1')
        self.assertIn(post1, posts, '`post1` should be in posts')