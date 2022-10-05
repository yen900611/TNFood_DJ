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


class PlacesSchema(Schema):
    name: str = "店家"
    address: str = "地址"
    phone_number: str = "電話"
    photos: Optional[list[str]]
    web_site: str = ""
    introduction: str = ""
    pub_date: datetime.datetime
    tag: list[Tags]
    devices = list[DeviceSchema]


@api.get("tags", response=List[Tags])
def tags(request):
    tag = Tag.objects.all()
    return tag


@api.post("tags")
def add_tag(request, pay_load: Tags):
    tag = Tag.objects.create(**pay_load.dict())
    return {"id": tag.id}


@api.get("places",
         response=List[PlacesSchema]
         )
def places(request):
    places = Place.objects.all().prefetch_related('photo_set', 'tag')
    # TODO refactor to Schema

    result = [PlacesSchema(
        **place.__dict__,
        tag=[Tags(display=t.name,value=t.style) for t in place.tag.all()],
        photos=[photo.file.url for photo in place.photo_set.all()]
    ) for place in places]
    return result


@api.get("place", response=PlacesSchema)
def get_place(request, id=1):
    place = Place.objects.prefetch_related('photo_set', 'tag').get(id=id)
    result = PlacesSchema(
        **place.__dict__,
        tag=[Tags(display=t.name,value=t.style) for t in place.tag.all()],
        photos=[photo.file.url for photo in place.photo_set.all()]
    )
    return result
