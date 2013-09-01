# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ...blog.models import Post
from ...tags.models import Tag

__author__ = 'Gennady Denisov <denisovgena@gmail.com>'


class BlogAdminTestCase(LiveServerTestCase):
    def setUp(self):
        # create admin user
        self.user = User.objects.create_superuser(
            'admin', 'admin@blog.com', 'adm1n')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + '/admin/')

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Spring Blog administration panel', body.text)

        #Login user
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.quit()

    def test_can_add_new_post_via_admin_site(self):
        # check if we are in site administration
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # check if posts link is present
        posts_links = self.browser.find_elements_by_link_text('Posts')
        self.assertEquals(len(posts_links), 1)

        # click on posts
        posts_links[0].click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 posts', body.text)

        # Find link 'add post'
        new_poll_link = self.browser.find_element_by_link_text('Add post')
        new_poll_link.click()

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Title:', body.text)
        self.assertIn('Tags:', body.text)
        self.assertIn('Is draft', body.text)
        self.assertIn('Date published:', body.text)

        # Add title, content and tags
        title_field = self.browser.find_element_by_id('id_title')

        # TinyMCE workaround
        current_handle = self.browser.current_window_handle
        self.browser.switch_to_frame('id_content_ifr')
        content_filed = self.browser.find_element_by_id('tinymce')
        content_filed.send_keys('Bar')
        self.browser.switch_to_default_content()

        tags_field = self.browser.find_element_by_id('id_tags_tag')
        title_field.send_keys('Foo')
        tags_field.send_keys('foo,bar,')

        save_button = self.browser.find_element_by_xpath('//input[@value=\'Save\']')
        save_button.click()

        self.assertEquals(Tag.objects.all().count(), 2)

        # Check if post has tags
        post = Post.objects.get(title='Foo')
        self.assertEquals(post.tags.all().count(), 2)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Posts', body.text)

        self.browser.get(self.live_server_url + '/admin/')
        # check if tags link is present
        tags_links = self.browser.find_elements_by_link_text('Tags')
        self.assertEquals(len(tags_links), 2)
        tags_links[1].click()

        foo_tag_link = self.browser.find_element_by_link_text('foo')
        foo_tag_link.click()

        body = self.browser.find_element_by_tag_name('body')

        self.assertIn('Name:', body.text)
