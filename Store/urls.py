from re import template
from django.urls import path
from Store.views import itemsView,detailsView,addCart
import Store.templates as Templates

urlpatterns = [
    path('store/', itemsView.as_view()),
    path('store/details/', detailsView.as_view()),
    path('store/add_cart/<int:id>', addCart)
]