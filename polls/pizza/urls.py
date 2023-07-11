from django.urls import path
from . import  views
urlpatterns=[
    path("send",views.send_email,name='send'),
    path('',views.index,name='index'),
       path('order',views.order,name='order')

    ]