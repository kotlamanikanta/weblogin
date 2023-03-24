from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password.'})
    else:
        if request.user.is_authenticated: 
            return redirect('home')
        else:
            return render(request, 'index.html')
                

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.create_user(username=username, email=email, password=password) 
        user.save()

        return redirect('home')
    return render(request,"registion.html")