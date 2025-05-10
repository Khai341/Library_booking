from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'REGISTRATION COMPLETE')
            return redirect('homepage')
        else:
            messages.error(request, 'REGISTRATION FAILED')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})

def custom_logout(request):
    logout(request)
    request.session.flush()  # Ensure session is fully cleared
    messages.success(request, 'You have been logged out.')
    return redirect('homepage')

def homepage(request):
    return render(request, 'layout.html')

# Create your views here.
