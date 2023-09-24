from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    context = {
        "posts":posts,
    }    
    return render(request, "blog/index.html", context)