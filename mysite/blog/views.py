from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.

class BlogListView(ListView):
    model = Blogs
    template_name = 'blog/index.html'
    context_object_name = 'data'
    ordering = ['-data_posted']
    paginate_by = 10
    

class BlogsDetailsView(DetailView):
    model= Blogs

class CreateBlogView(LoginRequiredMixin,CreateView):
    model = Blogs
    fields = ['title','content']
    login_url = 'login-page'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blogs
    fields = ['title','content']
    login_url = 'login-page'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class BlogsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Blogs
    success_url = '/' 
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

class ProfileBlogs(ListView):
    model = Blogs
    template_name = 'blog/index.html'
    context_object_name = 'data'
    
    paginate_by = 10
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blogs.objects.filter(author=user).order_by("-data_posted")

    

# def home(request):
#     data = Blogs.objects.all()
#     return render(request,'blog/index.html',{'data':data})

def about(request):
    return render(request,'blog/about.html', {'title':'About'})