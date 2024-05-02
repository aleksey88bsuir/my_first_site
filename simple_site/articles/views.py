from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth import logout
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
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


def login(request, user):
    return render(request, "articles/about.html", {'menu': menu, 'title': 'Регистрация'})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'articles/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('start_page')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'articles/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('start_page')


def logout_user(request):
    logout(request)
    return redirect('login')


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
