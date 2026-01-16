from django.urls import path
from .views import home, blog_list, blog_detail, blog_create

urlpatterns = [
    path('', home, name='home'), 
    path('blog', blog_list, name='blog_list'), 
    path('blog/<int:id>/', blog_detail, name='blog_detail'), 
    path('blog/create', blog_create, name='blog_create'),    
]