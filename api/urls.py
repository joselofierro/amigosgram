from django.urls import path
from api.views import *

urlpatterns = [
    path("categorias", CategoriaAPI.as_view(), name="list_pregunta_api"),
    path("number", number, name='number'),
    path("hello/<str:nombre>/<int:edad>", hello, name="saludo")
]
