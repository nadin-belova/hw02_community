from django.shortcuts import render, get_object_or_404

from posts.forms import PostForm
from .models import Group, Post, User
from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    # Если порядок сортировки определен в классе Meta модели,
    # запрос будет выглядеть так:
    # post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    # title = 'Yatube'
    # posts = Post.objects.all()[:10]
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    context = {
        # 'title': title,
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)


def profile(request, username):
    full_name = User.objects.get(username__exact=username)
    post_list = Post.objects.all().order_by('-pub_date')
    posts = Post.objects.order_by('-pub_date')
    post_count = posts.count()
    # author = get_object_or_404(User, username=username)
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'full_name': full_name,
        'post_count': post_count
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, pk=post_id)
    
    posts = Post.objects.filter(author=post.author)
    post_count = posts.count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    # if request.method == 'Post':
    #     form = PostForm(request.Post)
    #     if form.is_valid():
    #         post = form.save(commit = False)
    #         post.author = request.user
    #         post.save()
    #         return redirect('posts:profile', request.user)
    #     return render(request, 'posts/create_post.html', {'form': form}) 
    # else:
    #     form = PostForm()
    #     return render(request, 'posts/post_create.html', {'form': form})

    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
