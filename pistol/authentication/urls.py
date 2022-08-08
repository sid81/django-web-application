from django.urls import path
from . import views

urlpatterns = [
    path('',views.authenticatee,name='authenticate'),
    path('signout',views.signout,name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    
]
