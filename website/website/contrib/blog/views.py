from django.views.generic import ListView, DetailView

from parler.views import TranslatableSlugMixin

from .models import Post


class PostListView(ListView):
    model = Post
    queryset = Post.objects.published()
    paginate_by = 10


class PostDetailView(TranslatableSlugMixin, DetailView):
    model = Post
