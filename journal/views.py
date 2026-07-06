from django.shortcuts import render,redirect
from . forms import CreateUserForm

def home(request):
    return render(request, 'journal/index.html')

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = CreateUserForm()
    context = {"CreateUserForm": form}
    return render(request, 'journal/register.html', context)
        
            
            

def login(request):
    return render(request, 'journal/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'journal/dashboard.html')

