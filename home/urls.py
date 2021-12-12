
from home import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index,name = 'home'),
    path('about',views.about,name = 'about')
]
