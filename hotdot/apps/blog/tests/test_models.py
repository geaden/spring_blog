from django.test import TestCase
from django.utils import timezone

from ..models import Post
from ...tags.models import Tag


class PostTestCase(TestCase):
    def test_post_create(self):
        Post.objects.create(
            title=u'foo',
            content=u'bar',
            pub_date=timezone.now())

        self.assertEquals(
            Post.objects.all().
            count(),
            1)

    def test_create_post_with_tags(self):
        # Create some tags
        tag1 = Tag.objects.create(name='foo')
        tag2 = Tag.objects.create(name='bar')
        tag3 = Tag.objects.create(name='buz')
        # Create post with tags
        post = Post.objects.create(title='foo',
                                   content='bar')
        post.tags.add(tag1, tag2, tag3)
        post.save()
        updated_post = Post.objects.all()[0]
        self.assertEquals(3, updated_post.tags.count())

        # Clear tags
        updated_post.tags.clear()
        self.assertEquals(0, updated_post.tags.count())

