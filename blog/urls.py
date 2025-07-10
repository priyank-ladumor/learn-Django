from django.contrib import admin
from django.urls import path
from . import views 

#localhost:8000/blog
#localhost:8000/blog/learn
urlpatterns = [
    path('', views.learn_app, name='learn_app'),
    path('demo/', views.learn__app, name='learn__app'),
    path('list/', views.blog, name='blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
]
