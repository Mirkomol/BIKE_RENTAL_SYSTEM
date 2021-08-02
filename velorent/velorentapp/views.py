from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required  # we have used decorators for login required when entering


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was Created For' + user)

            return redirect('login')

    context = {'form': form}

    return render(request, 'velorentapp/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username Or Password is incorrect')

    context = {}

    return render(request, 'velorentapp/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# Calculate

def calculate(request):
    quantity = int(request.GET["Quantity"])
    tarif = int(request.GET["Tarif"])
    res = quantity * tarif
    return render(request, 'velorentapp/result.html', {'result':res})


# Message Handling Booking Form

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        get_date = request.POST.get('Date')
        get_time = request.POST.get('Time')
        adults = request.POST.get('Adults')
        tarif = request.POST.get('Tarif')
        text = request.POST.get('Message')
        all_text = f'Username: {name} \n Email: {email} \n Date: {get_date} \n Time: {get_time} \n Quantity: {adults} \n Tarif : {tarif} \n Message: {text}'

        print(all_text)

        subject = 'VeloRent'
        message = all_text
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['VelooRent@gmail.com']
        send_mail(subject, message, email_from, recipient_list, )
        return redirect('index')


def send_contact_message(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('usermail')
        phone = request.POST.get('userphone')
        text = request.POST.get('usermessage')
        all_text = f'{name}, {email}, {phone}, {text}'

        print(all_text)

        subject = 'VeloRent'
        message = all_text
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['VelooRent@gmail.com']
        send_mail(subject, message, email_from, recipient_list, )
        return redirect('contact')


@login_required(login_url='login')
def index(request):
    model = {
        'hour': Hour.objects.all(),
        'day': Day.objects.all(),
        'week': Week.objects.all(),
        'economy': Economy.objects.all(),
        'standard': Standard.objects.all(),
        'lux': Lux.objects.all(),
    }
    return render(request, 'velorentapp/index.html', model)


@login_required(login_url='login')
def bike(request):
    bikemodel = {
        'bikeeconomy': BikeEconomy.objects.all(),
        'bikestandard': BikeStandard.objects.all(),
        'bikelux': BikeLux.objects.all()
    }

    return render(request, 'velorentapp/bike.html', bikemodel)


@login_required(login_url='login')
def contact(request):
    return render(request, 'velorentapp/contact.html')
