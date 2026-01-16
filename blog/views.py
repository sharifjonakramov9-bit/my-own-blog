from django.shortcuts import render, redirect
from .models import Blog


def home(request):
    return render(request, 'home.html')


def blog_list(request):
    blogs = Blog.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        blogs = blogs.filter(title__icontain=search)

    if category:
        blogs = blogs.filter(category=category)

    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_list.html', {'blogs': blog})


def blog_create(request):
    if request.method == 'POST':
        Blog.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
        )
        return redirect('blog_list')
    
    return render(request, 'blog_create.html')
