from django.urls import path , include
from . import views
from django_email_verification import urls as email_urls



app_name = 'Users'
urlpatterns = [
    path('', views.account, name='account'),
    path('signup/', views.signup , name='signup'),
    path('logout/',views.logoutup , name='logoutup'),
   # path('signup/send-mail' , sendEmail, name='sendmail'),
    
    path('email/', include(email_urls)),

    
    
    
    
]