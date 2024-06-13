
from django.urls import path
from .  import views


urlpatterns = [
    path('', views.ind ),
    path('menu/', views.m ),
    
]