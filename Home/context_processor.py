from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from typing import Counter
from django.shortcuts import render, redirect
import json
from Stores.models import stores as stores_model
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count









def context_Processor(request):
    stores = stores_model.objects.all().annotate(ccount=Count('coupon',distinct=True)).annotate(ocount=Count('offers',distinct=True))
    unicategory = stores_model.objects.values('scategory').distinct().order_by().annotate(posts_count=Count('scategory'))
    randunicategory = random.sample(list(unicategory), 3)
    randstores = random.sample(list(stores), 4)
    #stores = stores_model.objects.all().annotate(ocount=Count('offers'),ccount=Count('coupon'))
    #ccount = stores_model.objects.all().annotate(ccount=Count('coupon'))
    #ocount = stores_model.objects.all().annotate(ocount=Count('offers'))
    context={}
    context['randunicategory']= randunicategory
    
    context['stores']= stores
    
    
    
    
    #login from all pages.
    if request.method == 'POST':
        password= request.POST.get('user-password')
        username= request.POST.get('user-name')
        user =  authenticate(request,username=username , password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Successfully Login!')
            #message ='save complete'
            print('a/n b/n c/n d/n')
            

      
     
            
 
    
    #context['ccount']= ccount
    #context['ocount']= ocount

    context['request']=request
    
    
    context['randstores']= randstores
    return context