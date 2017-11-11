from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Post

def index(request):
    context_dict = {}
    num_of_posts_per_page = 9

    # Categories.
    cats = Category.objects.all()
    context_dict['categories'] = cats

    # All posts.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    paginator = Paginator(posts, num_of_posts_per_page)
    recent_posts = get_paginator_page(request, paginator)
    context_dict['recent_posts'] = recent_posts

    # Featured post.
    featured_post = posts[0]
    context_dict['featured_post'] = featured_post

    # Category-sepcific page posts.
    # A wrapper dictionary is needed for a custom template filter key-value
    # lookup function which uses the category slug.
    cat_dict = {}
    for cat in cats:
        posts = Post.objects.filter(categories__name=cat.name).order_by(
                '-published_date')
        paginator = Paginator(posts, num_of_posts_per_page)
        cat_posts = get_paginator_page(request, paginator)
        cat_dict[cat.slug] = cat_posts
    context_dict['cat_dict'] = cat_dict

    return render(request, 'blog/index.html', context_dict)

def archive(request):
    context_dict = {}
    num_of_posts_per_page = 18

    # Grab all the posts, split them into pages, and add them to the context dictionary.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    paginator = Paginator(posts, num_of_posts_per_page)
    archived_posts = get_paginator_page(request, paginator)
    context_dict['archived_posts'] = archived_posts

    return render(request, 'blog/archive.html', context_dict)

def get_paginator_page(request, paginator):
    page = request.GET.get('page')
    try:
        page_content = paginator.page(page)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)
    return page_content
