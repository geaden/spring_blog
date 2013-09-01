from django.views.generic import DetailView, ListView

from .models import Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts_list'

    def get_queryset(self):
        # Display only published posts
        queryset = super(PostListView, self).get_queryset()
        return queryset.order_by('-pub_date').filter(is_draft=False)

