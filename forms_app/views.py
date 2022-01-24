from django.shortcuts import render
from .models import User
from . import forms
# Create your views here.
def index(request):
    context = {
        'django':'The Web Framework for Developers with a deadline'
    }
    return render(request,'index.html', context=context)

def signup(request):
    sign_up = forms.UserForm()
    if request.method == "POST":
        sign_up = forms.UserForm(request.POST)
        if sign_up.is_valid():
            sign_up.save(commit=True) 
            return index(request)

    data = {
        'form':sign_up,
    }
    return render(request,'signup.html',context=data)

def userlist(request):
    users = User.objects.order_by('name')
    data = {
        'users':users,
    }
    return render(request,'userlist.html',context = data)