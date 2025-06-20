from django.shortcuts import render, redirect
from .forms import RegisterForm  
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')  # ✅ or any success page you want
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {"form": form})
