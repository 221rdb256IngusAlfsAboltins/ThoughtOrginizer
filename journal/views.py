from django.shortcuts import render,redirect
from . forms import CreateUserForm, LoginForm, ThoughtForm,UpdateUserForm, UpdateProfileForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.views.decorators.cache import never_cache
from . models import Thought,Profile
from django.db import transaction

from django.contrib.auth.models import User

def home(request):
    return render(request, 'journal/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
         
            current_user = form.save()
            Profile.objects.create(user=current_user)
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
                return redirect('profile') 
            
        else:
            context = {"LoginForm": form}
            return render(request, 'journal/my_login.html', context)

  
    context = {"LoginForm":form}
    return render(request, 'journal/my_login.html',context)
       

@login_required(login_url='my_login')
def logout_user(request):
    if request.method == "POST":
        
        logout(request)
        return redirect('home') 
    
    return render(request, 'journal/logout_confirmation.html')


@login_required(login_url='my_login')
def profile_management(request):

    profile = Profile.objects.get(user=request.user)
    

    if request.method == "POST":
        form = UpdateUserForm(request.POST, instance=request.user)
        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid() and form_2.is_valid():
            with transaction.atomic():#abi vai neiviens netiek saglabaati ,gadijumā ja vienu no formām neizdodas saglabāt
                form.save()
                form_2.save()
            return redirect('profile')

    else:
        form = UpdateUserForm(instance=request.user)
        form_2 = UpdateProfileForm(instance=profile)

    context = {
        'profile': profile,
        'UpdateUserForm': form,
        'edit_mode': request.method == "POST",
        'ProfileUpdateForm': form_2,
    }

    return render(request, 'journal/profile.html', context)


@login_required(login_url='my_login')
def create_thought(request):

    if request.method == "POST":
        form = ThoughtForm(request.POST)
     
        if form.is_valid():
            thought = form.save(commit=False)  
            thought.user = request.user      
            thought.save()

            return redirect('my-thoughts') 

    else:
        form = ThoughtForm()

    context = {"ThoughtForm": form}
    return render(request, 'journal/create_thought.html', context)


@login_required(login_url='my_login')
def my_thoughts(request):
    AllThoughts = Thought.objects.all().filter(user=request.user)
    context = {'Thoughts': AllThoughts}
    return render(request, 'journal/my-thoughts.html',context)


@login_required(login_url='my_login')
def delete_thought(request):
    if request.method == "POST":
        selected = request.POST.getlist("thoughts")
        Thought.objects.filter(
            id__in=selected,
            user=request.user
        ).delete()
    return redirect('my-thoughts')


@login_required(login_url='my_login')
def view_thought(request, id):
    try:
        thought_inst = Thought.objects.get(
            pk=id,
            user=request.user
        )
    except:
        return redirect('my-thoughts')
    
    if request.method == "POST":
        form = ThoughtForm(request.POST, instance=thought_inst)

        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()

            return redirect('my-thoughts')

    else:

        form = ThoughtForm(instance = thought_inst)

    context = {"UpdateThoughtForm": form, "thought":thought_inst}
    return render(request, 'journal/view_thought.html', context)


@login_required(login_url='my_login')
def delete_account(request):
    if request.method == "POST":
        request.user.delete()
        return redirect('home')
    else:
        return render(request, 'journal/delete_account.html')
