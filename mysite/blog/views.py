from django.shortcuts import render
from .models import Blogs
# Create your views here.

def home(request):
    data = Blogs.objects.all()
    return render(request,'blog/index.html',{'data':data})

def about(request):
    return render(request,'blog/about.html', {'title':'About'})