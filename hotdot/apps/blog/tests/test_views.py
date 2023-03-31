from django.test import TestCase
from django.utils import timezone

from django.urls import reverse

from ..models import Post


class BlogViewsTestCase(TestCase):
    def setUp(self):
        self.post = Post.objects.\
            create(
                title=u'foo', content=u'bar',
                pub_date=timezone.now())
        self.detail_url = reverse(
            'detail',
            args=[self.post.pk])
        self.list_url = reverse(
            'list')

    def test_post_detail(self):
        response = self.client.\
            get(self.detail_url)

        self.assertEquals(
            response.status_code,
            200)

        self.assertEquals(
            response.context['object'],
            self.post)

    def test_post_list(self):
        # Create 10 more posts
        for i in range(10):
            Post.objects.create(title='foo %d' % i,
                                content='buz %d' % i,
                                pub_date=timezone.now())
        response = self.client.\
            get(self.list_url)

        self.assertEquals(
            response.status_code,
            200)

        self.assertEquals(
            len(response.context['posts_list']),
            10, msg='Posts per page should be 10')
        self.assertIn(self.post.pub_date.strftime('%A, %B %d, %Y'), response.content)

    def test_post_list_pagination(self):
        # Create 10 more posts
        for i in range(10):
            Post.objects.create(title='foo %d' % i,
                                content='buz %d' % i,
                                pub_date=timezone.now())

        response = self.client.get(self.list_url)

        self.assertIn('pager', response.content)
