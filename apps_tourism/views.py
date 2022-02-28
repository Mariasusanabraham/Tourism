from django.shortcuts import render, redirect
from django.contrib import messages
from apps_tourism.models import reg
from django.contrib.auth.models import auth
# Create your views here.


def home(request):
    return render(request, 'home.html')


def save(request):
    if request.method == 'POST':
        NAME = request.POST['name']
        EMAIL = request.POST['email']
        PASSWORD = request.POST['password']
        CONFIRM = request.POST['confirm']
        if PASSWORD == CONFIRM:
            y = reg(Name=NAME, Email=EMAIL, Password=PASSWORD,
                    Confirm_Password=CONFIRM)
            y.save()
            return render(request, 'login.html')
        else:
            messages.info(request, 'Password not matching')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def show(request):
    return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def show_log(request):
    return render(request, 'login.html')


def explore(request):
    return render(request, 'explore.html')


def places(request):
    return render(request, 'places.html')
