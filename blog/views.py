from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def home(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')


def get_post_by_name(request, name_post):
    data = {
        'name_post': name_post,
    }
    return render(request, 'blog/detail_by_name.html', context=data)


def get_post_by_number(request, number_post):
    data = {
        'number_post': number_post,
    }
    return render(request, 'blog/detail_by_number.html', context=data)