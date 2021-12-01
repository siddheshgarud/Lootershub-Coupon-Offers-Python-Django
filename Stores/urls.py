from django.urls import path
from . import views
from .models import stores



app_name = 'Stores'
urlpatterns = [
    path('', views.stores , name='stores'),
    path('coupons/', views.coupons, name='coupons'),
    #path('coupon/', views.coupon),
    path('<slug:stores_slug>',views.coupons, name='couponstores'),
    #path('<int:id',views.coupon_details,name='coupon_details'),
    path('category?<str:category>',views.stores,name='categories')
    
    
    
]