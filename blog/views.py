from django.shortcuts import get_object_or_404, render, redirect

from blog.forms import BlogForm
from .models import Blog


def home(request):
    return render(request, 'blog/home.html')


def blog_list(request):
    query = request.GET.get('q')
    blogs = Blog.objects.all().order_by('-created_at')

    if query:
        blogs = blogs.filter(title_icontains=query)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog_list.html', {'blogs': blog})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
        else:
            form = BlogForm()
        
        return render(request, 'blog/blog_create.html', {'form': form})