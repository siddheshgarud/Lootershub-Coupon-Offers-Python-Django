from django.shortcuts import render , get_object_or_404 , redirect
from django.http import Http404
from django.db.models import Q
import random
from django.db.models import Count
from django.template.defaulttags import register
from django.shortcuts import render
from .models import stores as stores_model
from .models import coupon as coupon_model
from .models import offers as offers_model
from .models import IPmodel
#from hitcount.views import HitCountDetailView



# Create your views here.
def stores(request,stores_name=None,category=None):
  
  
  #query for getting all stores & coupons
  
  stores = stores_model.objects.all().annotate(ccount=Count('coupon',distinct=True)).annotate(ocount=Count('offers',distinct=True))
  print(stores)
  coupons = coupon_model.objects.all()
  latestcoupons= coupon_model.objects.all().order_by('-cname')[:1]
  
  

  


  
  





  # for calculating number of coupons per stores 
  '''count_hit = True'''
  
  




#for getting unqiue 3-4 category and their stores count in /stores page
  unicategory = stores_model.objects.values('scategory').distinct().order_by().annotate(posts_count=Count('scategory'))
  randunicategory = random.sample(list(unicategory), 3)

  #for i in randunicategory:
    #print([i.scategory])
  
  if category:
    stores = stores.filter(scategory=category)
    
    if not stores:
        raise Http404
    #stores = stores.filter(scategory)
    
  


  if 'search' in request.GET:
    search = request.GET['search']
    print("hellow worlzhdhdh")
    stores = stores_model.objects.filter(stores_name__icontains=search).annotate(ccount=Count('coupon',distinct=True)).annotate(ocount=Count('offers',distinct=True))
    print(stores)
    
  
  
  
  
  
  
#context and return 
  context = {'stores': stores, 'latestcoupons':latestcoupons  }
  return render(request,'Stores/index.html', context)
  
  
  
  
  
def coupons(request,stores_slug=None):
  
  #St = None
  allstores = stores_model.objects.all()
  allcoupons = coupon_model.objects.all()
 
 #if there is ang slug then take objects from stotrs_model regarding slug
  if stores_slug:
    St = get_object_or_404(stores_model , slug=stores_slug )
   
   #filters all the product related to slug
    allcoupons = allcoupons.filter(cfid = St)
  #index(request , allcoupons)
   
  #for getting views of users
  def get_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
      ip = address.split(',')[-1].strip()
    else:
      ip = request.META.get('REMOTE_ADDR')
    return ip
  
  #IP = get_ip(request)
 # user = IPmodel(ip=IP)
#  result = IPmodel.objects.filter(Q(ip__icontains=IP))
#  if len(result)==1:
 #   pass
 # else:
  #  user.save()
  
  #counting users in models
 # countview = IPmodel.objects.all().count()
#  print(countview)
  
  
  
  
  return render(request,'Stores/coupons.html', {'allcoupons':allcoupons,'allstores':allstores,'St':St,})
  
#def coupon_details(request,id):
  #allcoupons = get_object_or_404(coupon_model , id=id)
  #return render(request,'Stores/coupons.html',{'allcoupons':allcoupons})






#for getting views of users





#def categories(request , cats):
  #categoriesproduct = stores_model.objects.all()
  #category = request.GET.get('categoriesproduct', None) 
  #print(categoriesproduct)
  #context = {'categoriesproduct':categoriesproduct}
  #return render(request , 'Stores/categories.html')
  