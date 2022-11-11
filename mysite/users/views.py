from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UsersRegistrationForm

# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = UsersRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('blog-home')
        else:
            messages.error(request, f"Something was wrong")
    else:
        form = UsersRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# type of messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error