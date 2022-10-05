from typing import List

from ninja import NinjaAPI, Schema, File
from ninja.files import UploadedFile
from .models import Place, Photo, Tag

api = NinjaAPI()


class Tags(Schema):
    name: str
    style: str


class Places(Schema):
    name: str
    address: str
    phone_number: str
    photos: list


@api.get("tags", response=List[Tags])
def tags(request):
    tag = Tag.objects.all()
    return tag

@api.post("tags")
def add_tag(request, pay_load:Tags):
    tag = Tag.objects.create(**pay_load.dict())
    return {"id":tag.id}

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