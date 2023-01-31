# import des fonction login et authenticate
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms 

def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ' '
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                massege = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'identifiants invalides'
    return render(request,'authentication/login.html',context={'form':form,'message':message})