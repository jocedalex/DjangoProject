from sqlite3 import Cursor
from django.shortcuts import render
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
        