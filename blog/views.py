from django.shortcuts import render
from .models import Blog

# Create your views here.

def learn_app(request):
    return render(request, 'blog/learn.html')

def learn__app(request):
    return render(request, 'blog/demo/index.html')

def blog(request):
    blogs = Blog.objects.all()
    print('blogs: ', blogs)
    return render(request, 'blog/list/index.html', {'blogs': blogs})

