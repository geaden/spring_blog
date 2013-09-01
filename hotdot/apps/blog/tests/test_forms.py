
from django.test import TestCase

from ..models import Post
from ..forms import PostAdminForm
from ...tags.models import Tag


class PostAdminFormTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title=u'foo',
                                        content=u'bar')
        for tag in ('foo', 'bar'):
            tag = Tag.objects.create(name=tag)
            self.post.tags.add(tag)

    def test_show_form(self):
        form = PostAdminForm(instance=self.post)
        self.assertEquals('foo', form['title'].value())
        self.assertEquals('foo,bar', form['tags'].value())