from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Item
from . import urls

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add(request):
    return render(request, 'add.html')

def item_list(request):
    items = item.objects.all()
    return render(request, 'index.html', { 'items':items })

class ItemList(ListView):
    model=Item
    

class ItemCreate(CreateView):
    model=Item
    fields= '__all__'
    
