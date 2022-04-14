from pyexpat import model
from datetime import date
import re
from sqlite3 import Cursor
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from .models import Cart, Item, Choosen, Order

# Create your views here.
class indexView(ListView):
    model=Item
    template_name='index.html'

class registerView(ListView):
    model=User
    template_name='registration/register.html'

class itemsView(ListView):

    model=Item
    second_model=Choosen
    template_name='store.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Django Store Joced Nieves'
        try:
            cartKey=Cart.objects.get(customer=self.request.user.id)
            total=0
            context['cart']=Choosen.objects.filter(cart=cartKey.id)
            for i in context['cart']:
                total += i.total
        except:
            total=0
            

        context['total']=total
        return context

class detailsView(ListView):

    model=Item
    second_model=Choosen
    template_name='details.html'

    def get_queryset(self):
        id = self.request.GET.get("id")
        qs = Item.objects.filter(id=id)
        return qs
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #cart_id=Cart.objects.filter(customer= context['user'].id)
        context['title']='Details Joced Nieves'
        #context['cart']=Choosen.objects.filter(cart=cart_id)
        return context
        
def addCart(request):
    
    
    try:
        cart_id=Cart.objects.get(customer=request.user.id)
        item=Item.objects.get(id=request.POST['id'])
        print(item.price)
        total=item.price * float(request.POST['qty'])
        article=Choosen(item=item,cart=cart_id,quantity=request.POST['qty'],total=total)
        article.save()
    except:
        cart=Cart(customer=request.user)
        cart.save()

        item=Item.objects.get(id=request.POST['id'])
        total=item.price * float(request.POST['qty'])
        article=Choosen(item=request.POST['id'],cart=cart.id,quantity=request.POST['qty'],total=total)
        article.save()

    return redirect('/store')

def addOrder(request):
    cart_id=Cart.objects.get(customer=request.user.id)
    selected_items=Choosen.objects.filter(cart=cart_id)
    order_details=[]

    for item in selected_items:
        order_details.append([item.id,item.quantity,item.total])

    order=Order(items=str(order_details),cart=cart_id.id,status='P',date=date.today(),delivery_date=date.today())
    order.save()
    selected_items.delete()

    return redirect('/store')

def registerUser(request):
    newpass=make_password(request.POST['password'])#formatting password
    user=User(username=request.POST['username'],first_name=request.POST['name'],last_name=request.POST['lastname'],email=request.POST['email'],password=newpass)
    user.save()
    return redirect('index')