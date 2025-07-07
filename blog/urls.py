from django.contrib import admin
from django.urls import path
from . import views 

#localhost:8000/blog
#localhost:8000/blog/learn
urlpatterns = [
    path('', views.learn_app, name='learn_app'),
    path('learn/', views.learn__app, name='learn__app'),
]
