# Create your views here.


from django.urls import path

from .views import \
    PostDetailView, PostListView


urlpatterns = [
    path(r'(?P<pk>\d+)/$',
        PostDetailView.as_view(),
        name='detail'),
    path(r'^$',
        PostListView.as_view(),
        name='list'),
]
