from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

from apps.perfiles.forms import SignUpForm, PerfilForm
from apps.perfiles.models import Perfil
from apps.posts.models import Post


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    # redirige al feed al usuario autenticado cuando accede a la vista login
    redirect_authenticated_user = True


"""def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'credenciales incorrectas'})
    return render(request, 'users/login.html')"""


# registra un usuario con validacion en el formulario
class SignUpView(FormView):
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')
    form_class = SignUpForm

    def form_valid(self, form):
        # validamos el formulario y guardamos el formulario
        form.save()
        return super().form_valid(form)


# vista para actualizar el perfil
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Perfil
    template_name = 'users/update_profile.html'
    # fields = ['website', 'biografia', 'telefono', 'imagen']
    form_class = PerfilForm

    def get_object(self, queryset=None):
        """objeto a actualizar o devolver actualizado"""
        return self.request.user.perfil

    def get_success_url(self):
        """return al perfil del usuario"""
        username = self.request.user.username
        return reverse('users:detail', kwargs={'username': username})


"""@login_required
def update_profile(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            # si el formulario no tiene error en la data
            # obtenemos la data
            data = form.cleaned_data
            print(data)
            perfil.website = data['website']
            perfil.biografia = data['biografia']
            perfil.telefono = data['telefono']
            perfil.imagen = data['imagen']

            perfil.save()
            messages.success(request, 'Perfil actualizado correctamente')
            # contruimos la url y la pasamos a redirect
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = PerfilForm()

    return render(request, 'users/update_profile.html', {'user': request.user,
                                                         'perfil': perfil,
                                                         'form': form})"""


# detalle del perfil del usuario y sus posts
class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    queryset = User.objects.all()

    # agregar los posts del usuario
    def get_context_data(self, **kwargs):
        # contexto si no hubieramos sobreeescrito el metodo
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context


@login_required
def logout_user(request):
    logout(request)
    return redirect('users:login')
