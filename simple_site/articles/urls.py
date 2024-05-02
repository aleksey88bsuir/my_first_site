from django.urls import path
from .views import *


urlpatterns = [
    path('', start_page, name='start_page'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('search', get_queryset, name='search'),
]
