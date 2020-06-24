from django.contrib import admin

# Register your models here.
from apps.preguntas.models import Pregunta


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'fecha', 'categoria')


admin.site.register(Pregunta, PreguntaAdmin)
