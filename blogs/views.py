from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from blogs.models import Post, Category

# Create your views here.

def home_page(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True)[:3]

    context = {
        'post_list': posts,
        'categories': categories,
        'featured': featured
    }

    return render(request, 'blogs/home_page.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

