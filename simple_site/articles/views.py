from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def start_page(reguest):
    return HttpResponse('Hello world!')


def display_all_articles(request):
    return HttpResponse('<h1>Отображение всех статей</h1>')


def article_by_id(request, article_id):
    return HttpResponse(f'<h1>Отображение всех статей</h1><p>{article_id}</p>')


def article_by_slug(request, article_slug):
    return HttpResponse(f'<h1>Отображение всех статей</h1><p>{article_slug}</p>')
