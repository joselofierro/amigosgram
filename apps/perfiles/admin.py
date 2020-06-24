from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from django.contrib.auth.models import User

from apps.perfiles.models import Perfil


# formulario de registro del modelo Perfil en el admin
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'website', 'imagen')
    search_fields = ('user__email', 'user__first_name')
    list_filter = ('created', 'modified',
                   'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Perfil', {
            'fields': (('user', 'imagen'),)
        }),

        ('Extra fields', {
            'fields': (('website', 'telefono'), 'biografia')
        }),

        ('Metadata', {
            'fields': (('created', 'modified'),)
        }),
    )

    readonly_fields = ('created', 'modified')


"""
Une los modelos de usuario y perfil para no tener 
que crear un usuario para asociarlo con un perfil
"""


class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'


class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


# sobreescribimos el admin user
admin.site.unregister(User)
# y registramos el admin perfil y user en uno solo
admin.site.register(User, UserAdmin)
