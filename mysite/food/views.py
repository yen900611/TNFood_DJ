from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Place

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
    return render(
        request,
        'food/index.html',
        {'store_list': places, 'photo': photo.file}
    )


def place_introduction(request, place_id: int):
    place = Place.objects.get(id=place_id)
    name = place.name
    address = place.address
    phone_number = place.phone_number
    web_site = place.web_site
    introduction = place.introduction
    return render(
        request,
        'food/place_introduction.html',
        {'store': place, 'name': name, 'address': address, 'phone_number': phone_number, 'web_site': web_site,
         'introduction': introduction},
    )
