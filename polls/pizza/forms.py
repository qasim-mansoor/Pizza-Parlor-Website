import django
from django.contrib.auth.models import User
from django import forms
from .models import order_that

class user_form(forms.ModelForm):
    class Meta:
        model=order_that
        fields=[
            'email',
            'phone_number',
            'name',
            'addres',

        ]