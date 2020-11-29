from django.shortcuts import render
from .forms import CreateGroupForm
from django.http import HttpResponseRedirect
from home.models import Account, Group, GroupBelongCategory, GroupHasAccount, Post
# Create your views here.

def grouplist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST, request.FILES, userName = request.user.id)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    #  Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'grouppages/list.html', {'form': form, 'Groups': Group.objects.all(), 'range': range(9)})

def detailGroup(request, id):
    posts = Post.objects.filter(groupId_id = id);
    return render(request, "grouppages/detailgroup.html", { "group": Group.objects.get(id=id), 'Posts': posts});