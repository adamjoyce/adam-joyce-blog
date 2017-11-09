from django.shortcuts import render
from django.utils import timezone

from .models import Category, Post

def index(request):
    context_dict = {}

    # Get all categories and posts and add them to the dictionary.
    cats = Category.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    featured_post = posts[0]
    context_dict['categories'] = cats
    context_dict['posts'] = posts
    context_dict['featured_post'] = featured_post

    # Add a list for posts in each category type.
    cat_dict = {}
    for cat in cats:
        post_list = Post.objects.filter(categories__name=cat.name).order_by(
                    '-published_date')
        cat_dict[cat.slug] = post_list

    context_dict['cat_dict'] = cat_dict
    print(context_dict)
    return render(request, 'blog/index.html', context_dict)
