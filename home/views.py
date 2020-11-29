from django.shortcuts import render
from .models import Category, Group, Account
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    account = Account.objects.get(user=request.user)
    avatar = 'media/{}'.format(account.avatar)
    data = {'Groups': Group.objects.all(), 'avatar': avatar}
    print(account.avatar)
    return render(request,'pages/home.html', data)
