from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView
from apps.preguntas.models import Pregunta


class QuestionList(ListView):
    template_name = 'vista1.html'

    def get(self, request, *args, **kwargs):
        # armamos el diccionario de preguntas
        preguntas = list(Pregunta.objects.values('texto', 'categoria__nombre'))

        # renderizamos el contexto en plantilla
        return render(request, self.template_name, {"preguntas": preguntas})
