from django.shortcuts import render, get_object_or_404

from .models import Group, Post


# delete this. RGenius
# def test(request):
#     text = '-------------------------------------'
#     # posts = Post.objects.filter(text__contains='Он')
#     posts = Post.objects.get(id=10)
#     # groups = Group.objects.all()

#     context = {
#         'text': text,
#         'posts': posts,
#         # 'groups': groups,
#     }
#     return render(request, 'posts/test.html', context)
# delete this. RGenius


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
    posts = Post.objects.all()
    #posts = Post.group(правильно или нет?)!!!!!
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
