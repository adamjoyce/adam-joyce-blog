from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    context_dict = {}
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    featured_post = posts[0]
    context_dict['posts'] = posts
    context_dict['featured_post'] = featured_post
    return render(request, 'blog/post_list.html', context_dict)
