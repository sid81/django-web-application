from django.contrib import admin
from django.urls import path
from cwh import views

urlpatterns = [
    path("",views.index,name='cwh'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact)  
]