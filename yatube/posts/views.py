from django.shortcuts import render, get_object_or_404

from .models import Group, Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = (Post.objects.filter(group=group))
    # posts = Post.objects.order_by('-pub_date')[:10]
    print(posts)
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request):
    template = 'posts/group_list.html'

    title = 'Yatube'

    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    posts = Post.objects.filter().order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # 'group': group,
        'posts': posts,
    }

    return render(request, template, context)
