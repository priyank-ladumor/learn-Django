from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def learn_app(request):
    return render(request, 'blog/learn.html')

def learn__app(request):
    return render(request, 'blog/demo/index.html')

def blog(request):
    blogs = Blog.objects.all()
    print('blogs: ', blogs)
    return render(request, 'blog/demo/index.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    # blog = Blog.objects.get(pk=blog_id)
    blog = get_object_or_404(Blog, pk=blog_id)
    print('blog: ', blog)
    return render(request, 'blog/details/index.html', {'blog': blog})

