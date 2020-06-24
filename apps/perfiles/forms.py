from django import forms
from django.contrib.auth.models import User

from apps.perfiles.models import Perfil


class SignUpForm(forms.Form):
    username = forms.CharField(
        min_length=4, max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation password'}))

    first_name = forms.CharField(
        min_length=2, max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(
        min_length=2, max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email = forms.CharField(
        min_length=6, max_length=70,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    # validar un campo en este caso el campo username
    def clean_username(self):
        # obtenemos el dato del campo
        username = self.cleaned_data['username']
        # validamos si existe ese usuario con el username,
        query = User.objects.filter(username=username).exists()
        # si existe
        if query:
            raise forms.ValidationError('Usuario ya existe')
        return username

    def clean_email(self):
        # obtenemos el valor del campo email
        email = self.cleaned_data['email']
        query = User.objects.filter(email=email).exists()
        if query:
            raise forms.ValidationError('Usuario con este email ya existe')
        return email

    # cuando un campo depende de otro campo para validarse
    def clean(self):
        """verificar que las contraseñas sean iguales"""
        # vamos a llamar al metodo antes de ser sobreescrito
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return data

    # registrar formulario con sus datos
    def save(self):
        # obtenemos todo los datos del formulario
        data = self.cleaned_data
        # eliminamos un campo que no necesitamos
        data.pop('password_confirmation')
        # creamos un usuario con todo el diccionario de datos
        user = User.objects.create_user(**data)
        perfil = Perfil.objects.create(user=user)
        perfil.save()


"""Formulario para terminar de actualizar perfil"""
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['website', 'biografia', 'telefono', 'imagen']

        labels = {
            'website': 'Website',
            'biografia': 'Biografia',
            'telefono': 'Telefono',
            'imagen': 'Imagen'
        }

        widgets = {
            'website': forms.URLInput(attrs={'class': 'form-control', 'required': True}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'imagen': forms.FileInput(attrs={'name': 'imagen', 'required': True})
        }
