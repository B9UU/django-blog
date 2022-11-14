from django.urls import path
from .views import BlogListView,BlogsDetailsView,CreateBlogView,UpdateBlogView,BlogsDeleteView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/<int:pk>', BlogsDetailsView.as_view(), name='blog-details'),
    path('blog/create', CreateBlogView.as_view(), name='blog-create'),
    path('blog/update/<int:pk>', UpdateBlogView.as_view(), name='blog-update'),
    path('blog/delete/<int:pk>',BlogsDeleteView.as_view(),name='blog-delete')
    
]