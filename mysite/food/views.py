from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Place, Photo, Tag, Tag_Management

# class StoreListView(generic.ListView):
#     model = Store
#     context_object_name = 'store_list'
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get the context
#         context = super(StoreListView, self).get_context_data(**kwargs)
#         # Create any data and add it to the context
#         context['some_data'] = 'This is just some data'
#         return context

from .models import Photo


# Create your views here.
def index(request):
    photo = Photo.objects.first()
    places = Place.objects.all()
    # tags = Tag.objects.first()
    tags = Tag.objects.all()
    return render(
        request,
        'food/index.html',
        {'store_list': places, 'photo': photo.file, 'tags': tags}
    )

#
# def form_filter(request):
#     tags = Tag.objects.all()
#     return render(request, 'food/form_filter.html', {'tags': tags})


def place_introduction(request, place_id: int):
    place = Place.objects.get(id=place_id)
    # 方法一
    # photo_list = Photo.objects.filter(place = place).all()
    # 方法二
    photo_list = place.photo_set.all()
    return render(
        request,
        'food/place_introduction.html',
        {'store': place,
         'photo_list': photo_list,
         },
    )
