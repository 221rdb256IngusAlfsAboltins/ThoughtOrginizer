from django.shortcuts import render


def home(request):
    return render(request, 'journal/home.html')

def register(request):
    return render(request, 'journal/register.html')

def login(request):
    return render(request, 'journal/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'journal/dashboard.html')

