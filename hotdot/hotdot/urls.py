from django.conf import settings
from django.urls import re_path, include
import django.views.static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mydjango_project.views.home', name='home'),
    # url(r'^mydjango_project/', include('mydjango_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^comments/', include('django_comments.urls')),

    # 3rd party urls
    re_path(r'^tinymce/', include('tinymce.urls')),

    # Your project url
    re_path(r'^', include('apps.blog.urls')),

    re_path(r'^', include('apps.tags.urls')),

    # serve static file on heroku
    re_path(r'^static/(.*)$',
            django.views.static.serve, {'document_root': settings.STATIC_ROOT}),
]
