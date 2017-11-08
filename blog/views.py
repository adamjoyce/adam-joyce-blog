from django.shortcuts import render
from django.utils import timezone

from .models import Category, Post

def index(request):
    context_dict = {}
    categories = Category.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    featured_post = posts[0]
    context_dict['categories'] = categories
    context_dict['posts'] = posts
    context_dict['featured_post'] = featured_post
    return render(request, 'blog/index.html', context_dict)
