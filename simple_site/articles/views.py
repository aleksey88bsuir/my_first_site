from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def start_page(reguest):
    return HttpResponse('Hello world!')
