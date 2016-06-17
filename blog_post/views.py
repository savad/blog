from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog_post.models import Blog, Tag


class BlogListView(ListView):
    """
    View for listing Blogs
    """
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class BlogDetailsView(DetailView):
    """
    View for rendering Blog detail
    """
    template_name = 'blog_detail.html'
    model = Blog
    context_object_name = 'blog'
