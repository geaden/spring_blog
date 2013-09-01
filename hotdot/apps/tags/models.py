# -*- coding: utf-8 -*-
from django.db import models

from ..blog.models import Post

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    def number_of_posts(self):
        return self.posts.all().count()

    number_of_posts.short_description = 'Posts'

    def __unicode__(self):
        return self.name
