import datetime
from typing import List, Optional

from django.contrib.auth import authenticate
from ninja import NinjaAPI, Schema, ModelSchema, Query, Router
from ninja.security import django_auth, HttpBearer, HttpBasicAuth

from .models import Place, Photo, Tag, Device

api = NinjaAPI(csrf=True)


class Visit_num(Schema):
    today: int
    total: int


class TagSchema(Schema):
    name: str
    value: str
    group: str


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
    web_site: str = "https://example.com"
    introduction: str = "店家資訊"
    pub_date: datetime.datetime
    tag: list[TagSchema]
    devices = list[DeviceSchema]


@api.get("tags", response=List[TagSchema])
def tags(request):
    # tags = Tag.objects.all()

    return [TagSchema(group=t.get_group_display(), name=t.name, value=t.value) for t in Tag.objects.all()]


# router = Router(auth=django_auth)


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        user = authenticate(username=username, password=password)
        return user


@api.post("tags", auth=BasicAuth())
def add_tag(request, tags: TagSchema):
    tag = Tag(name=tags.display, style=tags.value)
    tag.save()
    return tag.name


@api.get(
    "places",
    response=List[PlacesSchema])
def places(request, food_style: str = None):
    if food_style:
        places = Place.objects.prefetch_related('photo_set', 'tag').filter(tag__value=food_style)
    else:
        places = Place.objects.prefetch_related('photo_set', 'tag').all()
    result = [PlacesSchema(
        **place.__dict__,
        tag=[TagSchema(name=t.name, value=t.value,group=t.get_group_display()) for t in place.tag.all()],
        photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()]
    ) for place in places]
    return result


@api.get("place", response=PlacesSchema)
def get_place(request, id: int = 1):
    place = Place.objects.prefetch_related('photo_set', 'tag').get(id=id)
    result = PlacesSchema(
        **place.__dict__,
        tag=[TagSchema(name=t.name, value=t.value,group=t.get_group_display()) for t in place.tag.all()],
        photos=[PhotoSchema(name=photo.name, path=photo.file.url) for photo in place.photo_set.all()]
    )
    return result


@api.get("num_visits", response=Visit_num)
def visit_number(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return Visit_num(today=num_visits, total=num_visits)
