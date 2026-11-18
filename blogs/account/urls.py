# 127/0.0.1:8000
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<slug:slug>', views.blog_details, name='blog_details'),
    path('vision/', views.vision, name='vision'),  
    path('categories/<slug:slug>',views.blogs_by_category,name="blogs_by_category"),
    path('Blogers/',views.Blogers, name='Blogers'),
    
    ]