from sqlite3 import Cursor
from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Item

# Create your views here.
class itemsView(ListView):

    model=Item
    template_name='store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Django Store Joced Nieves'
        return context

class detailsView(ListView):

    model=Item
    template_name='details.html'

    def get_queryset(self):
        id = self.request.GET.get("id")
        qs = Item.objects.filter(id=id)
        return qs
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Details Joced Nieves'
        return context
        
def addCart(request,id):
    item=Item.objects.get(id=id)


    return redirect('/store')