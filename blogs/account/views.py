from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from account.models import Blogs,Category

def index(request):
    context = {
        "blogs": Blogs.objects.all(),
    }
    return render(request, 'account/index.html', context)

def blogs(request):
    context = {
        "blogs": Blogs.objects.all(), # veya mevcut listeniz/queryset'iniz
        "categories": Category.objects.all(),
        "selected_category": None
    }
    return render(request, "account/blogs.html", context)

def vision(request):
    return render(request, 'account/vision.html')

def Blogers(request):
    admins = User.objects.filter(is_admin=True, is_staff=True).annotate(blog_count=Count('blogs'))
    return render(request, 'account/Blogers.html', {'Blogers': admins})

def blog_details(request, slug):
    blog = Blogs.objects.get(slug=slug)
    
    
    return render(request, 'account/blog_details.html', {'blog': blog})

def blogs_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    
    context = {
        # Doğrudan Blog modeli üzerinden kategoriye göre filtreleme yapıyoruz:
        "blogs": Blogs.objects.filter(category=category, is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, 'account/blogs.html', context)

    
