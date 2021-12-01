from django.urls import path
from . import views


app_name = 'about'
urlpatterns = [
    #path('', views.index),
    path('contactus/', views.contactus , name = 'contactus'),
    path('privacypolicy/', views.privacypolicy, name = 'privacypolicy')
    #path('storesfilter/<str:strfilter>',views.index,name='stfier')
    
]