from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path, include

from .views import home, index, create, edit, update, delete, login, user_logout

urlpatterns = [
    path('',home),
    path('chittoor/',index),
    path('tirupati/',create),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),
    path('delete/<int:id>/',delete),
    path('login/',login),
    path('logout/',user_logout)
]
