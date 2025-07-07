from django.shortcuts import render

# Create your views here.

def learn_app(request):
    return render(request, 'blog/learn.html')

def learn__app(request):
    return render(request, 'blog/demo/index.html')

