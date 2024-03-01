from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('Главная страница')

def posts(request):
    return HttpResponse('Все посты блога')

def get_name_of_post(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')