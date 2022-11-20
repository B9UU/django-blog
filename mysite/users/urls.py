from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns = [
    
    path('register/', views.register, name='register-page'),
    path('login/',LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True),name='login-page'),
    path('logout/',LogoutView.as_view(),name='logout-page'),
    path('profile/',views.profile,name='profile-page'),
    path('password-reset/',PasswordResetView.as_view(template_name="users/password_reset.html"),
            name="password_reset"),

    path('password-reset/success/',PasswordResetDoneView.as_view(template_name='users/password_reset_success.html'),
        name='password_reset_done'),
        
    path('password-reset-confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    
]