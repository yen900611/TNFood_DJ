from typing import List

from ninja import NinjaAPI, Schema

from .models import Place, Photo, Tag

api = NinjaAPI()


class Tags(Schema):
    name: str
    style: str


class Places(Schema):
    name: str
    address: str
    phone_number: str
    photo_url: str


@api.get("tags", response=List[Tags])
def tags(request):
    tag = Tag.objects.all()
    return tag


@api.get("places")
def places(request, id):
    place = Place.objects.get(id=id)
    photo = place.photo_set.first()
    result = {
        'name': place.name,
        'address': place.address,
        'phone_number': place.phone_number,
        'photo_url': photo.file.url
    }
    return result
