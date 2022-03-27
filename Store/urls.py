from re import template
from django.urls import path
from Store import views
import Store.templates as Templates

urlpatterns = [
    path('store/', views.itemsView.as_view())
]