from django.shortcuts import render
from django.urls import reverse
from .models import Item, User
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class IndexView(View):
    """ Shows homepage with the list of all Item objects currently in db"""
    def get(self, request):
        items = Item.objects.all()
        return render(request, 'index.html', {'items': items})


class LikeView(View):
    """ Is used for 'like' functionality on homepage (uses POST request)"""
    def post(self, request, item_id):
        like_receiver = Item.objects.get(id=item_id)
        like_receiver.received_likes += 1
        like_receiver.save()
        return HttpResponseRedirect(reverse('index'))


class TopItemsView(View):
    """ Shows 'Top films' page with the list of 10 Item objects with the biggest number of received likes """
    def get(self, request):
        top_10_items = Item.objects.order_by('received_likes').reverse()[:10]
        return render(request, 'top_items.html', {'items': top_10_items})


class ActiveUsersView(View):
    """ Shows 'User activity' page with the list of all users ordered by the number of posted likes """
    def get(self, request):
        users = User.objects.order_by('posted_likes').reverse()
        return render(request, 'activity.html', {'users': users})


class LoginFormView(FormView):
    """ Shows Login page with the form """
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = '/'

    def form_valid(self, form):
        """ Checks if the submitted login form is valid """
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    """ Is used for 'logout' functionality in header (uses GET request) """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
