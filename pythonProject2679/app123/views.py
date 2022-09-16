from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from app123.forms import LoginForm, TaskForm
from app123.models import Task


def home(request):
    return render(request, 'home.html')


def card(request):
    return render(request, 'card.html')

def card(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'card_view.html',{'form':form})

def card_view(request):
    data = Task.object.all()
    return render(request,'card_view.html',{'data':data})


