from django.shortcuts import render
from .models import Site, Category, Tag, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request):
    site = Site.objects.first()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    page = request.GET.get('page', '')
    posts = Post.objects.all().filter(is_published=True)
    paginator = Paginator(posts, 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {
        'site': site,
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })


def category(request):
    site = Site.objects.first()
    requested_category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    page = request.GET.get('page', '')  # Get the current page number
    posts = Post.objects.filter(category__slug=slug).filter(is_published=True)
    paginator = Paginator(posts, 1)  # Showing 1 post for every page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {
        'site': site,
        'posts': posts,
        'category': requested_category,
        'categories': categories,
        'tags': tags,
    })


def tag(request):
    site = Site.objects.first()
    posts = Post.objects.filter(tag_slug=slug).filter(is_published=True)
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    page = request.GET.get('page', '')  # Get the current page number
    posts = Post.objects.filter(tag__slug=slug).filter(is_published=True)
    paginator = Paginator(posts, 1)  # Showing 1 post for every page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'tag.html', {
        'site': site,
        'posts': posts,
        'tag': requested,
        'categories': categories,
        'tags': tags,
    })


def post(request):
    site = Site.objects.first()
    requested_tag = Tag.objects.get(slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'post.html', {
        'site': site,
        'posts': posts,
        'tag': requested,
        'categories': categories,
        'tags': tags,
    })
