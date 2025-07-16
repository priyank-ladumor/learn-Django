from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

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


# @login_required 
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


