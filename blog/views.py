from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from random import randint

from .models import Category, Post

num_of_posts_per_page = 18

def index(request):
    context_dict = {}

    # Categories.
    cats = Category.objects.all()
    context_dict['categories'] = cats

    # All posts.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
            '-published_date')
    paginator = Paginator(posts, num_of_posts_per_page * 0.5)
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
        posts = Post.objects.filter(category__name=cat.name).order_by(
                '-published_date')
        paginator = Paginator(posts, num_of_posts_per_page)
        cat_posts = get_paginator_page(request, paginator)
        cat_dict[cat.slug] = cat_posts
    context_dict['cat_dict'] = cat_dict

    return render(request, 'blog/index.html', context_dict)

def archive(request, category_slug=None):
    context_dict = {}
    context_dict['category'] = category_slug

    # Categories for the footer.
    cats = Category.objects.all()
    context_dict['categories'] = cats

    if category_slug:
        category_slugs = []
        for cat in cats:
            category_slugs.append(cat.slug)

        # Is the category valid?
        if category_slug not in category_slugs:
            context_dict['category_missing'] = True
            return render(request, 'blog/archive.html', context_dict)
        else:
            # Grab posts that fall into the relevent category.
            posts = Post.objects.filter(
                    category__slug=category_slug).order_by('-published_date')
    else:
        # Grab all the posts.
        posts = Post.objects.filter(
                published_date__lte=timezone.now()).order_by(
                '-published_date')

    paginator = Paginator(posts, num_of_posts_per_page)
    archived_posts = get_paginator_page(request, paginator)
    context_dict['archived_posts'] = archived_posts

    print(context_dict['archived_posts'])
    return render(request, 'blog/archive.html', context_dict)

def post(request, category_slug, post_slug, random=False):
    context_dict = {}

    # Categories for the footer.
    cats = Category.objects.all()
    context_dict['categories'] = cats

    # The post being displayed.
    if not random:
        featured_post = Post.objects.filter(slug=post_slug)[0]
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now())
        featured_post = posts[randint(0, posts.count - 1)]
    context_dict['featured_post'] = featured_post

    return render(request, 'blog/post.html', context_dict)

def get_paginator_page(request, paginator):
    page = request.GET.get('page')
    try:
        page_content = paginator.page(page)
    except PageNotAnInteger:
        page_content = paginator.page(1)
    except EmptyPage:
        page_content = paginator.page(paginator.num_pages)
    return page_content
