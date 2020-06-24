from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Perfil(models.Model):
    # proxy model relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biografia = models.TextField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='users/imagen',
                               blank=True, null=True)

    def __str__(self):
        return self.user.username


"""@receiver(post_save, sender=User)
def create_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)      
def save_perfil(sender, instance, **kwargs):
    instance.perfil.save()"""


