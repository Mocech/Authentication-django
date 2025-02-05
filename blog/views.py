from django.shortcuts import render
from .models import Post

title= 'Login_System'
context = {
    'title':title
}

def home(request):
    return render(request, 'blog/home.html',context)

def blog(request):
  context = {
      'posts':Post.objects.all()
  }
  return render(request, 'blog/blog.html', context)

def about(request):
    return render(request, 'blog/about.html',{})