from django.db import models
from Stores.models import stores

# Create your models here.
'''class product(models.model):
  product_id= models.AutoField
  
  product_name = models.CharField(max_length=50)
  product_desc = models.CharField(max_length = 300)
  product_date = models.DataField()'''




class Banner(models.Model):
    bfid = models.ForeignKey(stores, on_delete=models.CASCADE , )
    bname = models.CharField(max_length = 100)
    bpercentage = models.IntegerField()
    bcategory= models.CharField(max_length=200)
    buses = models.IntegerField(default=0)
    bdesc = models.CharField(max_length=300)
    burl = models.CharField(max_length=500 , blank=True)
    bimage = models.ImageField(upload_to = "Home/" , default = "" ,)  
    def __str__(self):
      return self.bname


class Dealotd(models.Model):
  dealcompany = models.CharField(max_length=50)
  dealname = models.CharField(max_length=100)
  dealtag = models.CharField(max_length=50)
  dealtime = models.DateTimeField()
  
  dealurl = models.URLField()
  dealimage = models.ImageField(upload_to = "Home/" , default = "" ,)
  
  
  
