"""Collects data from vesna.yandex.ru"""
import urllib2
import urllib
import json
import random
import datetime
from copy import deepcopy

TAGS = ('mathematics', 'physics',
    'chemistry', 'polit')


VESNA_URL = 'http://vesna.yandex.ru/%s.xml'
SEPARATOR = '<!-- pagebreak -->'
START_PK = 1
POSTS = 12


def raw_vesna(tag, mix=False):
    """Gets data by provided tag

    :param tag: tag name
    :returns: plain html
    """
    url, tags = VESNA_URL % tag, [tag]
    if mix:
        tags = [TAGS[random.randint(
            0, len(TAGS) - 1)]
                for i in range(len(TAGS) - 1)]
        url, tags = mixed(tags)
    response = urllib2.urlopen(url).read()
    return response, tags

USER = [
    {
        "pk": 1,
        "model": "auth.user",
        "fields":
            {"username": "admin",
            "first_name": "",
            "last_name": "",
            "is_active": True,
            "is_superuser": True,
            "is_staff":     True,
            "last_login": "2013-08-31T19:51:00.361Z",
            "groups": [],
            "user_permissions": [],
            "password": "pbkdf2_sha256$10000$7Q57kNneSZh9$7LtQEfF67Fw2x7dTPG4s4VhvuDteuRMdvXjddDfQwAc=",
            "email": "denisovgena@gmail.com",
            "date_joined": "2013-08-31T19:46:40.574Z"}}]

def get_structure(tag, mixed):
    """
    Parses data and forms json

    :param tag: tag name
    :returns: json
    """
    response, tags = raw_vesna(tag, mixed)
    table = '<td colspan="9"'
    ' class="text">'
    start = response.find(table)
    end = response.find('</td>', start)
    post = response[start + len(table):end]
    # get title
    start = post.find('<h1')
    end = post.find('</h1>', start)
    title = post[start + len('<h1>'):end]
    # clean title
    garbage = title.find('>')
    title = title[garbage + 1:]
    # get text
    start = post.find('<p>')
    text = post[start + len('<p>'):]
    print text
    # insert page break
    if text.count('<p>') >= 2:
        # get first paragraph
        start = text.find('</p>', text.find('</p>'))
        end = text.find('<p>', start)
        before = text[:start] + '</p>' + '\n'
        after = text[end:-(len('</div>'))]
        text = before + SEPARATOR + after
    text = '<p>' + text
    result = {}
    result['tags'] = tags
    result['title'] = title
    result['text'] = text
    return result

def search_tags(tag, tags):
    """
    Get tag by provide tag name
    """
    for tag_obj in tags:
        if tag_obj['fields']['name'] == tag:
            return tag_obj
    return None

def mixed(tags):
    data = {'mix': urllib.quote(','.join(tags))}
    for tag in tags:
        data[tag] = 'on'
    return 'http://vesna.yandex.ru/all.xml?' + \
        urllib.urlencode(data), tags

def generate_fixture():
    """
    Generates django fixture for blog app
    """
    TIME = lambda: datetime.\
        datetime.now().isoformat() + "Z"
    TAGS_MODEL = 'tags.tag'
    POST_MODEL = 'blog.post'
    tags = []
    tag_dict = {
        'pk': 0,
        'model': TAGS_MODEL,
        'fields': {
            'name':'',
            'posts':[]
        }}
    posts = []
    post_dict = {
       "pk": 0,
       "model": POST_MODEL,
       "fields": {
           "title": "",
           "pub_date": TIME(),
           "created": TIME(),
           "modified": TIME(),
           "content": "",
           "is_draft": False
        }
    }
    i = START_PK
    j = START_PK
    for k in xrange(POSTS):
        for tag in TAGS:
            post_dict = deepcopy(post_dict)
            tag_dict = deepcopy(tag_dict)
            mixed = random.randint(0, 1)
            post = get_structure(tag, mixed)
            post_dict['pk'] = i
            post_dict['fields']['title'] = \
                post['title']
            post_dict['fields']['content'] = \
                post['text']
            posts.append(post_dict)
            for t in post['tags']:
                tag_obj = search_tags(t, tags)
                if tag_obj is None:
                    tag_dict['pk'] = j
                    tag_dict['fields']['posts'] = [i]
                    tag_dict['fields']['name'] = tag
                    tags.append(tag_dict)
                    j += 1
                else:
                    tag_obj['fields']['posts'].append(i)
            i += 1
    file = open('vesna_data.json', 'a')
    # get rid of duplicates
    for tag_obj in tags:
        tag_posts = set(tag_obj['fields']['posts'])
        tag_obj['fields']['posts'] = list(tag_posts)
    result = USER + posts + tags
    json.dump(result, file, indent=4)


if __name__ == '__main__':
    generate_fixture()





