from django.db import models
from django.core.files import storage
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='polls/static')
# Create your models here.
class get_os_info(models.Model):
    name_of_os=models.CharField(max_length=1300)
class order_that(models.Model):
    email=models.EmailField(unique=True)
    phone_number=models.IntegerField(max_length=200)
    name=models.CharField(max_length=20)
    addres=models.CharField(max_length=100)


class uploader(models.Model):
    name_of_item=models.CharField(max_length=200)
    price_of_item=models.IntegerField(max_length=50,null=True)
    img_of_item=models.ImageField(null=True,storage=fs)
    number_of_item=models.CharField(null=True,max_length=200)


# Create your models here.
