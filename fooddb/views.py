from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,DetailView,
                                    CreateView, DeleteView, UpdateView, 
                                    FormView, View)
# Login and Permissions
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from datetime import date
# local 
from fooddb import forms
from .models import Food


# CRUD Views
class FoodCreate(CreateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  model = Food
  form_class = forms.FoodForm
  template_name = 'fooddb/create.html'

  
  
class FoodList(ListView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  template_name = 'fooddb/list.html'
  model = Food
  context_object_name = 'all_foods'
  paginate_by = 10

  def get_queryset(self):
      #return Food.objects.filter(mealDate = date.today())
      return Food.objects.all()