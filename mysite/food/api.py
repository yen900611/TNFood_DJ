import datetime
from typing import List, Optional

from ninja import NinjaAPI, Schema, File, ModelSchema
from ninja.files import UploadedFile
from pydantic import AnyUrl

from .models import Place, Photo, Tag, Device

api = NinjaAPI()


class Tags(Schema):
    display: str
    value: str


class DeviceSchema(ModelSchema):
    class Config:
        model = Device
        model_fields = ['name']


class PhotoSchema(Schema):
    name: str = "photo"
    path: str = '/'


class PlacesSchema(Schema):
    id: int = 1
    name: str = "店家"
    address: str = "地址"
    phone_number: str = "電話"
    photos: Optional[list[PhotoSchema]]
    web_site: str = ""
    introduction: str = ""
    pub_date: datetime.datetime
    tag: list[Tags]
    devices = list[DeviceSchema]


@api.get("tags", response=List[Tags])
def tags(request):
    tags = Tag.objects.all()
    return [Tags(display=t.name, value=t.style) for t in tags]


@api.post("tags")
def add_tag(request, pay_load: Tags):
    tag = Tag.objects.create(**pay_load.dict())
    return {"id": tag.id}


@api.get(
    "places",
    response=List[PlacesSchema])
def places(request):
    places = Place.objects.prefetch_related('photo_set', 'tag').all()
    result = [PlacesSchema(
        **place.__dict__,
        tag=[Tags(display=t.name, value=t.style) for t in place.tag.all()],
        photos=[PhotoSchema(name=photo.name,path=photo.file.url) for photo in place.photo_set.all()]
    ) for place in places]
    return result


@api.get("place", response=PlacesSchema)
def get_place(request, id: int = 1):
    place = Place.objects.prefetch_related('photo_set', 'tag').get(id=id)
    result = PlacesSchema(
        **place.__dict__,
        tag=[Tags(display=t.name, value=t.style) for t in place.tag.all()],
        photos=[PhotoSchema(name=photo.name,path=photo.file.url) for photo in place.photo_set.all()]
    )
    return result
