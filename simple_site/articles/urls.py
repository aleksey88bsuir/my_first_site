from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page),
    path('all_articles', display_all_articles),
]
