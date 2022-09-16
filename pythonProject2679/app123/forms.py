from django import forms
from django.contrib.auth.forms import UserCreationForm

from app123.models import Login, Task


class LoginForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

