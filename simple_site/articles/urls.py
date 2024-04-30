from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page),
    path('all', display_all_articles, name='main_page'),
    path('all/<int:article_id>/', article_by_id, name='article_by_id'),
    path('all/<str:article_slug>/', article_by_slug, name='article_by_slug'),
]
