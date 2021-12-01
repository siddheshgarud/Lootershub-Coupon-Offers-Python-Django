from django.urls import include, path
from django.conf import settings
from . import views


app_name = 'Home'
urlpatterns = [
    path('', views.index , name='homepage'),
    path('basic', views.basic),
    path('category/<str:category>',views.index,name='categories'),
    #path('storesfilter/<str:strfilter>',views.index,name='stfier')
    
]

