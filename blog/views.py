from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] # сортирует по дате и выводит последние 5
    # или Blog.object.all() это все объекты
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

