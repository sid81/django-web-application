from django.shortcuts import render, HttpResponse

from .models import Destination

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
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'maya nagari'
    dest1.img= 'destination_1.jpg'
    dest1.price=700
    
    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'biriyani hub'
    dest2.img= 'destination_2.jpg'
    dest2.price=660
    
    dest3 = Destination()
    dest3.name = 'BBSR'
    dest3.desc = 'city of temple'
    dest3.img= 'destination_3.jpg'
    dest3.price=770
    
    dests = [dest1,dest2,dest3]
    
    return render(request,'index.html',{'dests':dests})