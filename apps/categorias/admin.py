from django.contrib import admin

# Register your models here.
from apps.categorias.models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


admin.site.register(Categoria, CategoriaAdmin)
