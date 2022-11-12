from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    
    path('register/', views.register, name='register-page'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login-page'),
    path('logout/',LogoutView.as_view(),name='logout-page'),
    path('profile/',views.profile,name='profile-page'),
]