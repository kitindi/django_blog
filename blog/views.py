from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {'posts': post}
    return render(request, 'index.html', context)


def article(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'article.html', {'post': post})