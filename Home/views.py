from django.shortcuts import render , redirect
import json
from django.contrib import messages
from Stores.models import stores as stores_model
from .models import Banner
from .models import Dealotd
import random
from django.db.models import Count




# Create your views here.
def index(request,category=None):
  stores = stores_model.objects.all().annotate(ccount=Count('coupon',distinct=True)).annotate(ocount=Count('offers',distinct=True))
  banners = Banner.objects.all()
  dealotd = Dealotd.objects.all()

  #check if product of specific category and show it
  if category:
    stores = stores.filter(scategory=category).annotate(ccount=Count('coupon',distinct=True)).annotate(ocount=Count('offers',distinct=True))
    
    
    if not stores:
        raise Http404
    #stores = stores.filter(scategory)
  simagegrid = stores_model.objects.all()
  
  
  
  
  
  context = { 'stores':stores,'banners':banners, 'simagegrid':simagegrid , 'Dealotd':dealotd }
 
 
 
 #search iperations
  if 'search' in request.GET:
    search = request.GET['search']
    stores = stores_model.objects.filter(stores_name__icontains=search)
    return redirect('Stores:stores' )
    
                  
  
  
  
  
  
  
  #searchfunction
  

      
  
  messages.success(request , 'This Website is Under Development So Some features May Not Work')
  return render(request,'Home/index.html',context)
















def basic(request):
  stores = stores_model.objects.all()
  
  
  unicategory = stores_model.objects.values('scategory').distinct().order_by().annotate(posts_count=Count('scategory'))

  
  
  #if category:
   # stores = stores.filter(scategory=category)
    #if not stores:
     #   raise Http404
    #stores = stores.filter(scategory)
  #for i in randunicategory:
   # print(i.scategory
    
   # )

  


  context = { }
  return render(request,'Home/basic.html',context)
  

