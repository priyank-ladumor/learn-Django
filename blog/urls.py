from django.contrib import admin
from django.urls import path
from . import views 

#localhost:8000/blog
#localhost:8000/blog/learn
urlpatterns = [
    path('', views.blog, name='blog'),
    path('demo/', views.learn__app, name='learn__app'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:blog_id>/update/', views.update_blog, name='update_blog'),  # Update blog
    path('<int:blog_id>/delete/', views.delete_blog, name='delete_blog'),  # Delete blog
]
