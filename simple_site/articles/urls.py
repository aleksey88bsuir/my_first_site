from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page, name='start_page'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('search', get_queryset, name='search'),
]
