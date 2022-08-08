from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.
def register(request):
    if request.method == "POST":
        
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']
       
        
        if User.objects.filter(username=username).exists():
            
            messages.info(request, "username already exists")
            return redirect('register')
           
        if User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return redirect('register')
        
        if password != pass2:
            messages.info(request, "Passwords didnot match")
            return redirect('register')
        
        if not username.isalnum():
            messages.info(request, "Username must be Alpha-Numeric!!")
            return redirect('register')
        
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        messages.info(request, "registred successfully")  
        print("user created")
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
         
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Successfully logged in")
            
        else:    
            messages.info(request, "Invalid credentials")
            return redirect('login')
    return render(request,'login.html')