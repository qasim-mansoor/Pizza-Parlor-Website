  
# Database
```python
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
```

A Web Application for a Pizza Parlor with modules including order generation, order tracking, bill generation and automated email generation. Backend built using the Django framework. Frontend build in HTML, CSS and JS.


