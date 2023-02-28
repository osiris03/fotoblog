
# import des fonction login et authenticate
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from django.conf import settings
#from django.views.generic import View
from . import forms 

# view base on class 
"""class LoginPage(View):
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

"""
# class base on function 

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
                login(request, user)
                return redirect('home')
            else:
                message = 'identifiants invalides'
    return render(request,'authentication/login.html',context={'form':form,'message':message})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})