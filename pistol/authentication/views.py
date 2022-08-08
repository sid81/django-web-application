from email.message import EmailMessage
from email.mime import message
from telnetlib import LOGOUT
from tkinter import E
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token


# Create your views here.
def authenticatee(request):
    return render(request,'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "username already exists")
            return redirect('signup')
           # return redirect('')
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            #return redirect('')
            return redirect('signup')
        if password != pass2:
            messages.error(request, "Passwords didnot match")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            #return redirect('home')
            return redirect('signup')
        
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your account has successfully created")
        
        
        #welcome email
          # Welcome Email
        subject = "Welcome to GFG- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ GFG - Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
             
        return redirect('signin')
    return render(request,'authentication/signup.html')


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')

def signin(request):
    
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         
         user=authenticate(username=username, password=password)
         
         if user is not None:
             
             login(request,user)
             firstname=user.first_name
             return render(request,'authentication/index.html',{'firstname':firstname})
         else:
             messages.error(request,"Invalid credentials")
             return redirect('signin')
    return render(request,'authentication/sigin.html')


def signout(request):
    logout(request)
    messages.success(request, "Loggedout successfully")
    return render(request,'authentication/index.html')