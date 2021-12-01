from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django_email_verification import send_email


# Create your views here.



def signup(request):
    form = CreateUserForm()
    
    
            
            
            
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        
        if form.is_valid():

            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Your Acoount is Created for' + user)
            return redirect('Users:signup')
            
        password= request.POST.get('user-password')
        username= request.POST.get('user-name')
        user =  authenticate(request,username=username , password=password)
        remember_me = request.POST.get('rememberme')
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Successfully Login!')
            
            print(remember_me)
            if remember_me is None:
              request.session.set_expiry(360)
              
            return redirect('Users:account')
        

        else:
            messages.warning(request, 'Username is Already Registered OR check password correctly')
            return redirect('Users:signup')


    context = {'form':form}
    return render(request,'Users/login.html', context)















def logoutup(request):
    logout(request)
    messages.success(request, 'Successfully Logout from Your Account!')
    return redirect('Users:signup')




def account(request):
    context = {}
    return render(request, 'Users/account.html',context)


def sendEmail(request):
    password= request.POST.get('password')
    username= request.POST.get('username')
    email = request.POST.get('email')
    user = get_user_model().objects.create(username=username, password=password, email=email)
    user.is_active = False
    send_email(user)
    return render(request , 'confirm_template.html')