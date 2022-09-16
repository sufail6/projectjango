
from django.urls import path

from app556 import views

urlpatterns = [
    path('',views.home,name='home'),
    path('teacher_register',views.teacher_register,name='teacher_register'),
    path('login_view',views.login_view,name='login_view'),
    path('admin_panal',views.admin_panal,name='admin_panal'),
    path('card',views.card,name='card'),
    path('card_view', views.card_view, name='card_view'),
]
