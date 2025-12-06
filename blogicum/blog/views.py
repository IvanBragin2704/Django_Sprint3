from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    current_time = timezone.now()
    template = 'blog/index.html'

    post_list = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).select_related(
        'category',
        'author',
        'location'
    ).order_by('-pub_date')[:5]

    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    current_time = timezone.now()

    post = get_object_or_404(
        Post.objects.select_related('category', 'author', 'location'),
        pk=id,
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    )

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    current_time = timezone.now()

    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = category.posts.filter(  # ← Вот оно!
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
