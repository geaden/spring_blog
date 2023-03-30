from django.conf import settings
from django.conf.urls import include, url

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
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('django_comments.urls')),

    # 3rd party urls
    url(r'^tinymce/', include('tinymce.urls')),

    # Your project url
    url(r'^', include('apps.blog.urls',
                      namespace='blog',
                      app_name='blog')),

    url(r'^', include('apps.tags.urls',
                      namespace='tag',
                      app_name='tag')),

    # serve static file on heroku
    url(r'^static/(.*)$',
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
]
