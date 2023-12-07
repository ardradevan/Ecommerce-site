from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os
from django.db import models

import datetime
# importing validationerror
from django.core.exceptions import ValidationError
 
# creating a validator function
def validate(value):
   

    if  not value.isnumeric():
        return value
    else:
        raise ValidationError("This field access only characters")

def get_file_path(request,filename):
    orinal_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,orinal_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False,validators =[validate]) 
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keyword=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.CharField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        slug=models.CharField(max_length=150,null=False,blank=False)
        name=models.CharField(max_length=150,null=False,blank=False) 
        image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
        small_description=models.CharField(max_length=250,null=False,blank=False)
        quantity=models.IntegerField(null=False,blank=False)
        description=models.TextField(max_length=500,null=False,blank=False)
        original_price=models.FloatField(null=False,blank=False)
        selling_price=models.FloatField(null=False,blank=False)
        status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
        trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
        tag=models.CharField(max_length=150,null=False,blank=False)
        meta_title=models.CharField(max_length=150,null=False,blank=False)
        meta_keyword=models.CharField(max_length=150,null=False,blank=False)
        meta_description=models.CharField(max_length=500,null=False,blank=False)
        created_at=models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateField(auto_now_add=True)
