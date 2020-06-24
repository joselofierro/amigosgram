from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.perfiles.models import Perfil


class Post(models.Model):
    """ Post model. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # es necesario hacer estar relacion si necesito acceder a datos del perfil
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=False)
    titulo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        """ Return title and username """
        return f'{self.titulo} by @{self.user.username}'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like de {self.user.username} al {self.post.titulo}'
