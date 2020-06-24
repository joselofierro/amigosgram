from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField(max_length=20)

    def __str__(self):
        return self.nombre
