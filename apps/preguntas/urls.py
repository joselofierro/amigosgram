from django.urls import path
from apps.preguntas.views import *

app_name = 'preguntas'
urlpatterns = [
    path('listado', QuestionList.as_view(), name='preguntas')
]
