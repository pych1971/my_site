from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def home(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return HttpResponse('Все посты блога')


def get_post_by_name(request, name_post):
    return HttpResponse(f'Информация о посте {name_post}')


def get_post_by_number(request, number_post):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number_post}')
