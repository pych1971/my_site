from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def get_name_of_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')


def get_post_by_number(request, number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
