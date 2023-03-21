from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,"index.html")

def registion(request):
    return render(request,"registion.html")