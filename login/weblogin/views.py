from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=User.objects.create_user(username=username,password=password) 
        user.save()
        
        return redirect('home')
    return render(request,"index.html")                  

def register(request):
    if request.method=='POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.create_user(username=username, email=email, password=password) 
        user.save()

        return redirect('home')
    return render(request,"registion.html")