from django.shortcuts import render
from django.urls import reverse
from .models import Item
from django.views.generic import ListView


class IndexView(ListView):
    model = Item
    template_name = 'index.html'
