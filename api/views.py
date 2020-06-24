from django.http import JsonResponse, HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api.serializers import *


# Create your views here.

def number(request):
    # debugger en la terminal
    # import pdb; pdb.set_trace()
    # obtengo los numeros y los separo
    numeros = request.GET.get("nu").split(",")
    # los convierto en una lista de enteros y los ordeno
    numeros = sorted(map(int, numeros))
    return JsonResponse({"numbers": numeros})


def hello(request, nombre, edad):
    if edad < 12:
        mensaje = "Hola {}, no estas autorizado".format(nombre)
    else:
        mensaje = "Hola {}, estas autorizada".format(nombre)
    return HttpResponse(mensaje)


class CategoriaAPI(ListCreateAPIView):
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        query = Categoria.objects.all()
        # parametro que viene por url
        parameter = self.request.GET.get("q")
        if parameter is not None:
            query = query.filter(nombre__icontains=parameter)

        return query
