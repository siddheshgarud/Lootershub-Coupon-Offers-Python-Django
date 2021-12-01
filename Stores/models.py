from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import UserManager
from django.urls import reverse
import datetime
from django.db.models.aggregates import Count
from hitcount.models import HitCountMixin, HitCount
from django_resized import ResizedImageField


def randomString():
    um = UserManager()
    return( um.make_random_password( length=25 ) )


#calculating usercount
#class userview(models.Model):
   #IP = models.CharField(max_length= 100 ,default=None)
   #def __str__(self):
    #return self.IP


class IPmodel(models.Model):
  ip = models.TextField(max_length=100)
  def __str__(self):
    return self.ip



# Create your models here.
class stores(models.Model):
  
  
  #id = models.AutoField(primary_key=True)
  sfid = models.ForeignKey
  stores_name = models.CharField(max_length=50)
  slug = models.CharField(max_length=25, default=randomString , unique = True)
  sdesc = models.CharField(max_length = 100 , default ="")
  simage = models.ImageField(upload_to = "Store/images/stores" , default = "")
  sresimage = ResizedImageField(size=[370, 250],upload_to = "Store/images/stores" , default = "")
  scategory = models.CharField(max_length=100 , default="")
  ssubcategory = models.CharField(max_length=100 , default= "")
  
  sdatetime = models.DateTimeField()
  viewcount = models.ManyToManyField(IPmodel ,related_name = "stores_views",blank=True)

  def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]
  
  '''def save(self, *args, **kwargs):
    self.scategory = self.scategory.lower()
    return super(User, self).save(*args, **kwargs)'''
  
  class Meta:
        ordering = ('-stores_name',)
  def __str__(self):
    return self.stores_name
  
  def get_absolute_url(self):
     return reverse('Stores:couponstores', args=[str(self.slug)])
     
  def get_absolute_url_category(self):
    return reverse('Stores:categories',args=[str(self.scategory)])
  
class offers(models.Model):
  ofid = models.ForeignKey(stores, on_delete=models.CASCADE)
  oname = models.CharField(max_length = 100)
  opercentage = models.IntegerField()
  ocategory= models.CharField(max_length=200)
  ouses = models.IntegerField(default=0)
  odesc = models.CharField(max_length=300)
  ourl = models.CharField(max_length=500 , blank=True)
  oimage = models.ImageField(upload_to = "Store/images/stores/offers" , default = "" , blank=True)  
  def __str__(self):
    return self.oname
    
    
    
    
    
    
  
class coupon(models.Model):
  #id =models.AutoField(primary_key=True)
  cfid = models.ForeignKey(stores, on_delete=models.CASCADE)
  cname = models.CharField(max_length = 100)
  cdetails = models.CharField(max_length = 200 , default="")
  cpercentage = models.IntegerField()
  cverify = models.BooleanField(default=True)
  ccode = models.CharField(max_length= 100,  default="abcd")
  ccategory= models.CharField(max_length=200)
  ccrdatetime = models.DateTimeField(null=True, blank=True)
  # cexdatetime = models.DateTimeField(null=True, blank=True)
  def __str__(self):
    return self.cname
  def get_absolute_url(self):
    return reverse('Stores:coupon',args=[self.id,])
    
    



  

