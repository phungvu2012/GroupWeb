from django.shortcuts import render, redirect
from .forms import UserForm
from home.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def register(request):
    userFormInput = UserForm()
    authenticationForm = AuthenticationForm()
    if request.method == 'POST':
        if UserForm(request.POST):
            userFormInput = UserForm(request.POST)
            if userFormInput.is_valid():
                userFormInput.save()
                return HttpResponseRedirect('/')
        if AuthenticationForm(data=request.POST):
            authenticationForm = AuthenticationForm(data=request.POST)
            if authenticationForm.is_valid():
                user = authenticationForm.get_user()
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'user': userFormInput, 'form': authenticationForm})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})