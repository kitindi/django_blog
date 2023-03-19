from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {'posts': post}
    return render(request, 'index.html', context)


def articles(request):
	return render(request, 'articles.html')


def article(request):
	return render(request, 'article.html')