from django.http import HttpResponse
from django.shortcuts import render

from .models import Photo


# Create your views here.
def index(request):
    # return HttpResponse("Hello food!")
    photo = Photo.objects.first()
    return render(request, 'food/index.html', {'place_nums': range(6),'photo':photo.file })
