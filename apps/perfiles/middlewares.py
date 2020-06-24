"""middleware que valida si un usuario tiene una biografia
    o foto de perfil -> api de bajo nivel que modifica el objeto request
    o response
"""
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletationMiddleware:
    """initializacion del middleware"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """se ejecuta por cada request antes de llegar a la vista.

            el login redirige al feed pero el feed si se ve afectado
            por el middleware de actualizar datos.
        """
        if not request.user.is_anonymous:
            perfil = request.user.perfil
            # print(perfil)
            if not perfil.imagen or not perfil.biografia:
                if request.path not in [reverse('users:update_profile'), reverse('users:logout')] \
                        and not request.path.startswith('/admin/'):
                    return redirect('users:update_profile')

        response = self.get_response(request)
        return response
