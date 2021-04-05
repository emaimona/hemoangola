from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import Donor

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'index.html')

def regist(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username') 
            messages.success(request, 'benvenue ' + user)
            return redirect('url_login')
    
    content = {'form': form}
    return render(request, 'regist.html', content)

def find(request):
    data = Donor.objects.all()

    content = {'d': data}
    return render(request, 'find.html', content)

def about(request):
    return render(request, 'about.html')

def v404(request):
    return render(request, '404.html')

def login_user(request):
    content = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('url_home') 
        else:
            messages.info(request, 'user or pass wrong')
            
    return render(request, 'login.html', content)

def logout_user(request):
    logout(reuest)
    return redirect('url_login')
