from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm, ThoughtForm  
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.views.decorators.cache import never_cache

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
    print("Tessstinnggg2")
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
       

def logout_users(request):
    if request.method == "POST":
        print(request.user)  # should show username before logout
        logout(request)
        return redirect('home') 
    
    return render(request, 'journal/logout_confirmation.html')


@login_required(login_url='my_login')
def profile(request):
    return render(request, 'journal/profile.html')


@login_required(login_url='my_login')
def create_thought(request):

    if request.method == "POST":
        form = ThoughtForm(request.POST)
     
        if form.is_valid():
            print("testng")
            thought = form.save(commit=False)  # Don't save to DB yet
            thought.user = request.user       # Attach logged-in user
            thought.save()

            return redirect('dashboard')  # Redirect after success

    else:
        form = ThoughtForm()

    context = {"ThoughtForm": form}
    return render(request, 'journal/create_thought.html', context)
