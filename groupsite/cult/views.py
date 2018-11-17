from django.shortcuts import render
from django.urls import reverse
from .models import Item
from django.views.generic import ListView
from django.db.models import F
from django.http import request

class IndexView(ListView):
    model = Item
    template_name = 'index.html'

    # if request.GET.get('Next') == 'Next':
    #     print('user clicked summary')


