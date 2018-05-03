from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task, Department, Vehicle
from django.contrib.auth.models import User
from .forms import LoginForm

def login_view(request):
    lfrom = LoginForm(request.POST or None)
    if lfrom.is_valid():
        username = lfrom.cleaned_data.get("username")
        password = lfrom.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/home/')
    return render(request, 'pd/login.html', {"form": lfrom})

def home_view(request):
    return render(request, 'pd/home.html')


def history_view(request):
    return render(request, 'pd/task.html')

def vehicle_view(request):
    car = Vehicle.objects.all()
    return render(request, 'pd/vehicles.html', {"car": car})

def logout_view(request):
    logout(request)
    return redirect('/')
