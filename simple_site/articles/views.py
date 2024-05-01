from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
# Create your views here.

menu = ['Главная', 'Обратная связь', 'О сайте', 'Регистрация']


def start_page(reguest):
    published_articles = Article.objects.filter(is_published=True)

    return render(reguest, "articles/index.html",
                  {'menu': menu,
                   'title': 'Главная страница',
                   'posts': published_articles})


def about(reguest):
    return render(reguest, "articles/about.html", {'menu': menu, 'title': 'О сайте'})


def display_all_articles(request):
    return HttpResponse('<h1>Отображение всех статей</h1>')


def article_by_id(request, article_id):
    return HttpResponse(f'<h1>Отображение всех статей</h1><p>{article_id}</p>')


def article_by_slug(request, article_slug):
    return HttpResponse(f'<h1>Отображение всех статей</h1><p>{article_slug}</p>')
