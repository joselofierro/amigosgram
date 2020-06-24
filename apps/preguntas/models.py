from django.db import models

# Create your models here.
from apps.categorias.models import Categoria


class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateField('Fecha de publicación')
    categoria = models.ForeignKey(Categoria, related_name='preguntas', on_delete=models.DO_NOTHING)
