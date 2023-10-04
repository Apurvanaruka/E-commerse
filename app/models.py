from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,)
    sub_category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="ecommerse/pimg")
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)
    def __str__(self) -> str:
        return self.name

class UserCreateFrom(UserCreationForm):
    email = forms.EmailField(required=True,label="Email",error_messages={'exists':'Email is Exists'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')   

    def __init__(self, *args, **kwargs):    
        super(UserCreateFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs={'class':'full-control','placeholder': 'Email address'}
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conferm Password'          
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Email is already exists')
        return self.cleaned_data['email']
    
class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    def __str__(self) -> str:
        return self.email

class Order(models.Model):
    image = models.ImageField(upload_to='ecommerces/order/image')
    product = models.CharField(max_length=100,default='')
    quantity = models.IntegerField()
    price = models.IntegerField()
    total = models.CharField(max_length=1000,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    pincode = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    date_time = models.DateTimeField(default=datetime.datetime.today)    

    def __str__(self):
        return self.product
    
