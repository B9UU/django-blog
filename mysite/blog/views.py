from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Blogs
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


# def home(request):
#     data = Blogs.objects.all()
#     return render(request,'blog/index.html',{'data':data})

def about(request):
    return render(request,'blog/about.html', {'title':'About'})