from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('posts/', views.posts),
    path('posts/<int:number_post>/', views.get_post_by_number),
    path('posts/<str:name_post>/', views.get_post_by_name),
]
