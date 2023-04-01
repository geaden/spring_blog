# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ...blog.models import Post
from ...tags.models import Tag

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class SpringBlogLiveTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url)

    def test_scrolling(self):
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('No posts', body.text)

        # Create some posts
        for i in range(5):
            post = Post.objects.create(
                title=u'Foo',
                content=u'<p>Foo</p><!-- pagebreak --><p>Bar</p>'
            )

        self.browser.get(self.live_server_url)

        self.browser.find_element_by_link_text('more...').click()

        body = self.browser.find_element_by_tag_name('body')

        self.assertIn('No comments', body.text)

        name_field = self.browser.find_element_by_name('name')
        email_field = self.browser.find_element_by_name('email')
        comment_field = self.browser.find_element_by_name('comment')
        name_field.send_keys('foo')
        email_field.send_keys('foo@bar.bz')
        comment_field.send_keys('foo bar bz')

        self.browser.find_element_by_xpath(
            '//input[@value=\'leave a comment\']').click()

        body = self.browser.find_element_by_tag_name('body')

        self.assertNotIn('No comments', body.text)

        self.assertIn('foo said:', body.text)
