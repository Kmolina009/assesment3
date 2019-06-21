from django.urls import path, reverse
from . import views
from .models import Item

urlpatterns = [
 path('', views.ItemList.as_view(), name='item_list'),
 path('create/', views.ItemCreate.as_view(), name='item_create'),
]