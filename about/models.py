from django.db import models

from django import forms

# Create your models here.
class webinfo(models.Model):
  waboutus = models.CharField(max_length= 500)
  wtitle = models.CharField(max_length= 100)
  wlogo = models.ImageField(upload_to = "about/images/logo" , default = "")
  wemail = models.TextField(max_length=199)
  
  
  
  
class developers(models.Model):
  dname = models.CharField(max_length= 100)
  dprofession = models.CharField(max_length= 50)
  dlinkedin = models.URLField(max_length= 100)
  dcontact = models.IntegerField()
  dphoto = models.ImageField(upload_to = "about/images/dphoto" , default = "")




class ContactForm(forms.Form):
  first_name = forms.CharField(max_length = 50)
  last_name = forms.CharField(max_length = 50)
  email_address = forms.EmailField(max_length = 150)
  message = forms.CharField(widget = forms.Textarea, max_length = 2000)