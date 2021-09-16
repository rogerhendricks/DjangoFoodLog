from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,DetailView,
                                    CreateView, DeleteView, UpdateView, 
                                    FormView, View)
# Login and Permissions
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from datetime import date
from django.core import serializers
# local 
from food import forms
from .models import Food, DailyFood


# Error Pages
def permission_denied_view(request, exception):
    return render(request, 'errors/403.html')

# Base pages.
class MealPageView(LoginRequiredMixin,TemplateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  template_name = 'food/index.html'

  def get_context_data(self, **kwargs):
    user = self.request.user.id
    context = super(MealPageView, self).get_context_data(**kwargs)
    d = Food.objects.filter(client = user).values()
    context['data'] = list(d)
    return context



class AboutPageView(TemplateView):
    template_name = 'about.html'

# CRUD Views
class FoodCreate(CreateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  model = Food
  form_class = forms.FoodForm
  template_name = 'food/create.html'

  def get_context_data(self, **kwargs):
    user = self.request.user.id
    context = super(FoodCreate, self).get_context_data(**kwargs)
    d = Food.objects.filter(client = user, favorite=True).values()
    context['data'] = list(d)
    return context



  def form_valid(self, form):
    form.instance.client = self.request.user
    return super().form_valid(form)
  
  
class FoodList(ListView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  # template_name = 'food/list.html'
  template_name = 'food/table.html'
  model = Food
  context_object_name = 'all_food'
  paginate_by = 10

  def get_queryset(self):
      #return Food.objects.filter(mealDate = date.today())
      return Food.objects.all()

class FavoriteList(ListView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  # template_name = 'food/list.html'
  template_name = 'food/favList.html'
  model = Food
  context_object_name = 'all_favorites'
  paginate_by = 10

  def get_queryset(self):
      return Food.objects.filter(favorite=True)
      #return Food.objects.all()


class FoodUpdate(UpdateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  model = Food
  form_class = forms.FoodForm
  template_name = 'food/update.html'