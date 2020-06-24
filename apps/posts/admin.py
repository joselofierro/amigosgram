from django.contrib import admin

# Register your models here.
from apps.posts.models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'titulo', 'foto')
    search_fields = ('titulo',)
    readonly_fields = ('created', 'modified')