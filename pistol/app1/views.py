from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Destination
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    #return HttpResponse("Hello MOTO")
    return render(request,'home.html')
def add(request):
    
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'results.html',{'result':res})#json format/dict=key:value pair

def index(request):
    dests=Destination.objects.all()
    
    return render(request,'index.html',{'dests':dests})





    
    




