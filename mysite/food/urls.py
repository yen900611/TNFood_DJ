from django.shortcuts import render
from django.urls import path, include
# from .views import index, place_introduction
from .api import api
from .views import place_introduction


def index(request):
    return render(request, 'food/index.html')


# def place_introduction(request):
#     return render(request,'food/place_introduction.html')

urlpatterns = [
    path('', index, name='food_index'),
    path('<int:place_id>/', place_introduction, name='food_introduction'),
]
