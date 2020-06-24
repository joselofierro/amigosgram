import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# List post
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from apps.posts.forms import PostForm
from apps.posts.models import Post, Like

# create post
"""@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form,
                                                      'user': request.user,
                                                      'perfil': request.user.perfil})"""


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'posts/create_post.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    # añadir el usuario y perfil al contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['perfil'] = self.request.user.perfil

        return context


# lista de posts en el feed
class ListPostView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'


# detalle de un post
class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail_post.html'
    context_object_name = 'post'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Post.objects.all()


# agrega o elimina de likes en un posts
@login_required
def likes_posts(request):
    if request.method == 'GET':
        i_username = request.GET.get('user')
        i_post = request.GET.get('post')
        like = Like.objects.filter(user_id=i_username, post_id=i_post).exists()
        if like:
            Like.objects.filter(user_id=i_username, post_id=i_post).delete()
        else:
            like = Like(user_id=i_username, post_id=i_post)
            like.save()

        data = {'like_count': Like.objects.filter(post_id=i_post).values('user__username').count()}

        return HttpResponse(json.dumps(data, ensure_ascii=False),
                            content_type="application/json; encoding=utf-8")
