from django.shortcuts import render
from django.http import HttpResponse, response
from django.template import loader
from .models import order_that, uploader,get_os_info
from .forms import user_form
import os
from twilio.rest import Client
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
import random
def send_email(request):
    subject = request.POST.get('email')
    message1 = request.POST.get('name')
    message2 = request.POST.get('phone_number')
    message3 = request.POST.get('addres')
    massage=name+"phone number\n"+massage2+"addres\n"+massage3
    from_email = 'az4860364@gmail.com'
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['p190119@nu.edu.pk'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        all_field=uploader.objects.all()

        img=list()
        price=list()

        template = loader.get_template('index.html')
        content={
        'all_field':all_field,

    }


        text={}
        return HttpResponse(template.render(content, request))

def order(request):
    answer=None
    bill=list()
    final_bill=None
    #answer = request.GET('email' ,False)
    #for e in answer:
     #   bill.append(e)

    email = request.POST.get('get_the_order')
    answer=email

    final_bill=uploader.objects.filter(name_of_item=answer)

    answer=None
    bill=list()
    final_bill=None
    #answer = request.GET('email' ,False)
    #for e in answer:
     #   bill.append(e)

    email = request.POST.get('get_the_order')
    answer=email

    final_bill=uploader.objects.filter(name_of_item=answer)
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            random_number=random.randint(982398238,1000000000000)
            messages.success(request,'   THANKS FOR YOU OREDR order has been place and your order number is :: {}'.format(random_number))
            send_mail(
        'pizza delivery',
        'thanks for your order.we will short deliver your pizza. HAPPY DAY and enjoy',
        'az4860364@gmail.com',
        ['p190119@nu.edu.pk'],
        fail_silently=False,)
            w=os.getcwd()
            makeit=os.path.join(w,"test123")
            os.mkdir(makeit)




            form.save()




    content={'form':form,
    'final_bill':final_bill,

            }
    return render(request,'order.html',content)
def index(request):
    all_field=uploader.objects.all()
    content={
        'all_field':all_field,

    }
    template = loader.get_template('index.html')


    text={}
    return HttpResponse(template.render(content, request))