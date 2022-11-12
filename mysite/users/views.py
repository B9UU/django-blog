from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UsersRegistrationForm, ProfileImageForm, ProfileUpdateForm
from django.contrib.auth import login


# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = UsersRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            user = form.save()
            login(request, user)
           
            return redirect('blog-home')
        else:
            messages.error(request, f"Something was wrong")
    else:
        form = UsersRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required(login_url='login-page')
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST,instance=request.user)
        pwd_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.usersprofile)
        if form.is_valid() and pwd_form.is_valid():
            form.save()
            pwd_form.save()
            messages.success(request,'Your account has ben updated')
            return redirect('profile-page')

    else:
        form = ProfileUpdateForm(instance=request.user)
        pwd_form = ProfileImageForm(instance=request.user.usersprofile)
    context = {
        'p_form':form,
        "pwd_form":pwd_form,
    }
    return render(request, 'users/profile.html',context)

# type of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error