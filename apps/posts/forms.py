from django import forms

from apps.posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['user', 'perfil', 'titulo', 'foto']

        labels = {
            'titulo': 'Titulo',
            'foto': 'Foto'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'foto': forms.FileInput(attrs={'required': True})

        }
