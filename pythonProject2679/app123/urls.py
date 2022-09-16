from django.urls import path

from app123 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('card',views.card,name='card'),
]