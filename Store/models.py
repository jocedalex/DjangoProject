from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here..

class Category(models.Model):
    id=models.PositiveIntegerField(primary_key=True,blank=False,null=False,verbose_name="ID")
    name=models.CharField(blank=False,max_length=15,verbose_name="Name")

    def __str__(self):
        return '{}'.format(self.name)

class Item(models.Model):
    id=models.PositiveIntegerField(primary_key=True,blank=False,null=False,verbose_name="ID")
    name=models.CharField(blank=False,max_length=15,null=False,verbose_name="Name")
    description=models.CharField(blank=False,max_length=50,null=False,verbose_name="Description")
    category=models.ForeignKey(Category,blank=False,null=False,on_delete=models.CASCADE,verbose_name="Category")
    picture=models.CharField(null=False,default='',verbose_name='Picture',max_length=20)
    price=models.FloatField(blank=False,null=False,verbose_name="Price")
    available=models.IntegerField(verbose_name="Available units")

    def __str__(self):
        return '{}'.format(self.name)

class Cart(models.Model):
    id=models.PositiveIntegerField(primary_key=True,blank=False,verbose_name="ID")
    customer=models.ForeignKey(User,blank=False,null=False,on_delete=models.CASCADE)

class Choosen(models.Model):
    id=models.PositiveIntegerField(primary_key=True,blank=False,null=False)
    item=models.ForeignKey(Item,blank=False,null=False,verbose_name="Item",on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,blank=False,null=False,verbose_name="Cart",on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(blank=False,null=False,verbose_name="Quantity")
    total=models.FloatField(blank=False,null=False,verbose_name="Total Price")


class Order(models.Model):
    id=models.PositiveIntegerField(primary_key=True,blank=False,verbose_name="ID")
    item=models.ForeignKey(Item,blank=False,null=False,verbose_name="Item",on_delete=models.PROTECT)
    cart=models.ForeignKey(Cart,blank=False,null=False,verbose_name="Cart",on_delete=models.PROTECT)
    status=models.CharField(max_length=1)
    date=models.DateField(blank=False,null=False,verbose_name="Creation Date")
    delivery_date=models.DateField(blank=False,null=False,verbose_name="Delivery Date")