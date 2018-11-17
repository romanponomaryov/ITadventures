from django.shortcuts import render
from django.urls import reverse
from .models import Item, User
from django.views.generic import ListView
from django.db.models import F
from django.http.request import HttpRequest


class IndexView(ListView):
    model = Item
    template_name = 'index.html'


