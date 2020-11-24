from django.shortcuts import render
from .models import Category, Group
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/register')
    
    data = {'Groups': Group.objects.all()}
    return render(request,'pages/home.html', data)