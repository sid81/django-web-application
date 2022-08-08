from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("this is 2022")
    
def about(request):
    return HttpResponse("sultan 2016")
def contact(request):
    return HttpResponse("tvf pitchers 2015")