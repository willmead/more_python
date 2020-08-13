from django.views import generic
from .models import Post
from datetime import datetime
from django.shortcuts import redirect


class PostsView(generic.ListView):
    template_name = 'postsapp/posts.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        """Return all published posts."""
        return Post.objects.all().order_by('-datetime')


def new_post(request):
    new_post = Post(body=request.POST['post_body'], user=request.POST['post_user'], datetime=datetime.now())
    new_post.save()
    return redirect('postsapp:posts')
