# import des fonction login et authenticate
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms \

# view base on class 
class LoginPage(View):
    form_class = forms.LoginForm #class formulaire de connection
    template_name = 'authentication/login.html' # chemin du gabarie utiliser par la vue
    def get(self, request):
        form = self.form_class()
        message = ' '
        return render(request,self.template_name,context={'form':form,'message':message})

    def post(self, request):
         form = self.form_class(request.POST)
         message = ''
         if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'identifiants invalides'
            return render(request,self.template_name,context={'form':form,'message':message})


# class base on function 

def logout_user(request):
    logout(request)
    return redirect('login')

"""
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
                login(request, user)
                return redirect('home')
            else:
                message = 'identifiants invalides'
    return render(request,'authentication/login.html',context={'form':form,'message':message})
"""