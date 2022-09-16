from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from app556.forms import Loginform, TaskForm
from app556.models import Task


def home(request):
    return render(request, 'home.html')


def teacher_register(request):
    form = Loginform()
    if request.method == 'POST':
        form = Loginform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            messages.info(request, '')
            return redirect('home')
    return render(request, 'teacher_register.html', {"form": form})


def login_view(request):
    return render(request, 'login.html')


def admin_panal(request):
    return render(request, 'adminhome.html')


def card(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panal')
    return render(request, 'card.html',{'form':form})

def card_view(request):
    data = Task.objects.all()
    return render(request,'card_view.html',{'data':data})
