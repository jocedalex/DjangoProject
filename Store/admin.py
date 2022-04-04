from msilib.schema import ListView
from django.contrib import admin
from .models import Customer,Choosen,Cart,Category,Item,Order

# Register your models here.
@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display=('id','first_name','email','phone')
    ordering = ('id',)
    search_fields=('id','first_name','email','phone')
    list_per_page= 20

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','name')
    ordering = ('id',)
    search_fields=('id','name')
    list_per_page= 20

@admin.register(Item)
class itemAdmin(admin.ModelAdmin):
    list_display=('id','name','category','price','available')
    ordering = ('id',)
    search_fields=('id','name')
    list_filter=('category',)
    list_per_page= 20

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display=('id','customer')
    ordering = ('id',)
    search_fields=('id','customer')
    list_per_page= 20

@admin.register(Choosen)
class choosenAdmin(admin.ModelAdmin):
    list_display=('id','item','quantity','total')
    ordering = ('id',)
    search_fields=('id','item')
    list_per_page= 20

@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display=('id','item','status')
    ordering = ('id',)
    search_fields=('id','item')
    list_per_page= 20
