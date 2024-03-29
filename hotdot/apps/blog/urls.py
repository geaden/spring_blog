# Create your views here.


from django.urls import re_path

from .views import \
    PostDetailView, PostListView


urlpatterns = [
    re_path(r'(?P<pk>\d+)/$',
            PostDetailView.as_view(),
            name='detail'),
    re_path(r'^$',
            PostListView.as_view(),
            name='list'),
]
