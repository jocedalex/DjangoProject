from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from Store.views import indexView,itemsView,detailsView,addCart,addOrder,registerUser
import Store.templates as Templates


urlpatterns = [
    path('',login_required(indexView.as_view()),name='index'),
    path('store/', login_required(itemsView.as_view()),name="store"),
    path('store/details/', login_required(detailsView.as_view())),
    path('store/add_cart/', login_required(addCart), name='add_cart'),
    path('store/add_order/', login_required(addOrder), name='checkout'),
    path('accounts/login/',LoginView.as_view(),name='login'),
    path('accounts/register/',registerUser,name='register'),
    path('logout/',logout_then_login,name='logout')
]