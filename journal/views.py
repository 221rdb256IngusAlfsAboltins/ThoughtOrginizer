from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def home(request):
    return render(request, 'journal/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User created!")
            return redirect('my_login')
        
    context = {"CreateUserForm": form}
    return render(request, 'journal/register.html', context)
        
            
            

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
  
    context = {"LoginForm":form}
    return render(request, 'journal/my_login.html',context)
       
@login_required(login_url='my_login')
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home') 
    
    return render(request, 'journal/logout_confirmation.html')

@login_required(login_url='my_login')
def dashboard(request):
    return render(request, 'journal/dashboard.html')

