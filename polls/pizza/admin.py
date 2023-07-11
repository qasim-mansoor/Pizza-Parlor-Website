from django.contrib import admin
from django.db import models
from pizza.models import  order_that, uploader,get_os_info

# Register your models here.
admin.site.register(get_os_info)
admin.site.register(uploader)
@admin.register(order_that)
class order_check(admin.ModelAdmin):
    list_display=('email','name','addres','phone_number')
    search_fields=['name']
# Register your models here.
