from unicodedata import name
from django.contrib import admin
from django.urls import path
from itistudent.views import *

app_name = "itistudent"   


urlpatterns = [
    path("", myhome, name="homepage"),
    path("register/", addusertoadmin, name="register"),
    path('list/', trackList.as_view(),name='list'),
    path('user/', userList.as_view(),name='user'),
    path('show/',show,name='show'),
    path('insert/',studentInserting,name='insert'),
    path('delete/<int:id>',delete,name='delete'),
    path('add/',add,name='add'),
    path('update/<int:id>',update,name='update'),
    path("login/",loginuserandadmin,name="login"),
    path("logout", logout_request, name= "logout"),
    
]