from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import EditProfile, EditAvatar
from django.contrib import messages
from home.models import Account
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
 
def edit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    form = EditProfile()
    if request.method == "POST":
        if(request.user.is_authenticated):
            form = EditProfile(request.POST, userName = request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('account/')
    return render(request, "pages/edit.html", {"form": form})


def change_avatar(request):
    form = EditAvatar()
    if request.method == 'POST':
        form = EditAvatar(request.POST, request.FILES)
        if form.is_valid():
            accountUser = Account.objects.get(user = request.user)
            print('form: ', form.cleaned_data['avatar'])
            accountUser.avatar = form.cleaned_data['avatar']
            accountUser.coverPhoto = form.cleaned_data['coverPhoto']
            accountUser.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/editavatar.html', {'form': form})

def change_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/account/changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pages/editpassword.html', {
        'form': form
    })
