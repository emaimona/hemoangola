from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .forms import CreateUserForm, DonorForm
from .models import Donor

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import fill_m, fill_p

# Create your views here.
def home(request):
    return render(request, 'index.html')

def regist(request):
    data = {
        'm' : 'Bengo',
        'fill_p': fill_p(),
        'fill_m': fill_m()
    }
    form = DonorForm()
    
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request, 'benvenue ' + user)
            return redirect('url_login')
    
    content = {'form': form, 'data': data}
    return render(request, 'regist.html', content)

def find(request):
    data = Donor.objects.all()[:5]

    content = {'d': data}
    return render(request, 'find.html', content)

def about(request):
    return render(request, 'about.html')

def v404(request):
    return render(request, '404.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        try:
            user = Donor.objects.get(username=username, password=password)
            if user is not None:
                return render(request,'index.html', {'user': user}) 
        except Exception:
            messages.info(request, 'user or pass wrong')
            
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('url_login')

@login_required(login_url='url_login')
def perfil(request):
    pass




'''
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('url_teste')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = CreateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'teste.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
    
@transaction.atomic
def registar(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user = user_form.cleaned_data.get('username') 
            messages.success(request, 'benvenue ' + user)
            return redirect('url_login')
        else:
            messages.error(request,'Please correct the error below.')
    
    content = {'user_form': user_form, 'profile_form': profile_form, 'fill_m': fill_m()}
    return render(request, 'teste.html', content)

@login_required
@transaction.atomic
def update_profile2(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect('url_teste')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = CreateUserForm()
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'teste.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    '''