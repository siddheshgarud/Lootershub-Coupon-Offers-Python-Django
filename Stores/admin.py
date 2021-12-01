from django.contrib import admin
from .models import stores
from .models import coupon ,IPmodel ,offers

# Register your models here.
admin.site.register(stores)
admin.site.register(coupon)
admin.site.register(IPmodel)
admin.site.register(offers)