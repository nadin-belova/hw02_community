from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:10]
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    posts = Post.objects.filter(group=group)
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Yatube'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }

    return render(request, template, context)
