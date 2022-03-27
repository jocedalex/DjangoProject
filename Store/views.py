from sqlite3 import Cursor
from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

# Create your views here.
class itemsView(ListView):
    model=Item
    template_name='store.html'