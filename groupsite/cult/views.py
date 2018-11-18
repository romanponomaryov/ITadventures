from django.shortcuts import render
from django.urls import reverse
from .models import Item, User
from django.db.models import F
from django.http import HttpResponseRedirect


def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def like(request, item_id):
    like_receiver = Item.objects.get(id=item_id)
    like_receiver.received_likes += 1
    like_receiver.save()
    return HttpResponseRedirect(reverse('index'))


def top_items(request):
    top_10_items = Item.objects.order_by('received_likes').reverse()[:10]
    return render(request, 'top_items.html', {'items': top_10_items})


