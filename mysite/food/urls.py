from django.urls import path, include
from .views import index, place_introduction
from .api import api

urlpatterns = [
    path('', index, name='food_index'),
    path('<int:place_id>/', place_introduction, name='food_introduction'),
]
