from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.db.models import Q
# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def start_page(request):
    published_articles = Article.objects.filter(is_published=True)
    context = {'menu': menu,
               'title': 'Главная страница',
               'posts': published_articles,
               }
    return render(request, "articles/index.html", context=context)


def about(request):
    return render(request, "articles/about.html", {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render(request, "articles/about.html", {'menu': menu, 'title': 'Контакты'})


def login(request):
    return render(request, "articles/about.html", {'menu': menu, 'title': 'Регистрация'})


def show_post(request, post_id):
    post = Article.objects.get(pk=post_id)
    context = {'menu': menu,
               'title': 'Статья',
               'post': post}
    return render(request, "articles/post.html", context=context)


def get_queryset(request):
    search_param = request.GET.get('q')
    search_query = Q(title__icontains=search_param) | Q(author__icontains=search_param) | Q(
        content__icontains=search_param) & Q(is_published=True)
    published_articles = Article.objects.filter(search_query)
    context = {'menu': menu,
               'title': 'Главная страница',
               'posts': published_articles,
               }
    return render(request, "articles/index.html", context=context)
