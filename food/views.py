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
from django.db import transaction
from django.shortcuts import redirect
# local 
from food import forms
from .models import Food

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
    #d = Food.objects.filter(client = user).values()
    d = Food.objects.filter(client = user).select_related('food').values(
      'mealDate',
      'food__name',
      'food__calories', 
      'food__fat_ratio', 
      'food__carb_ratio',
      'food__protein_ratio'
      )
    context['data'] = list(d)
    return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

# CRUD Views
# class FoodCreate(CreateView):
#   login_url = '/accounts/login/'
#   redirect_field_name = 'redirect_to'
#   model = Food
#   form_class = forms.FoodForm
#   template_name = 'food/create.html'

#   def get_context_data(self, **kwargs):
#     user = self.request.user.id
#     context = super(FoodCreate, self).get_context_data(**kwargs)
#     d = Food.objects.filter(client = user, favorite=True).values()
#     context['data'] = list(d)
#     return context

#   def form_valid(self, form):
#     form.instance.client = self.request.user
#     return super().form_valid(form)
  
  
# class FoodList(ListView):
#   login_url = '/accounts/login/'
#   redirect_field_name = 'redirect_to'
#   template_name = 'food/table.html'
#   model = Food
#   context_object_name = 'all_food'
#   paginate_by = 10

#   def get_queryset(self):
#       return Food.objects.all()


# class FavoriteList(ListView):
#   login_url = '/accounts/login/'
#   redirect_field_name = 'redirect_to'
#   template_name = 'food/favList.html'
#   model = Food
#   context_object_name = 'all_favorites'
#   paginate_by = 10

#   def get_queryset(self):
#       return Food.objects.filter(favorite=True)
      #return Food.objects.all()


class FoodUpdate(UpdateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  model = Food
  form_class = forms.FoodForm
  template_name = 'food/update.html'




class FoodAdd(LoginRequiredMixin, TemplateView):
    # permission_required = ('app.change_client')
    # login_url = '/accounts/login/'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = Food
    template_name = 'food/testFoodCreate.html'

    def get(self, *args, **kwargs):
      user = self.kwargs.get('username')
      print(user)
      formset = forms.FoodFormSet(queryset=Food.objects.none(), initial=[{'client': user}] ,auto_id=False) # initial={'client': user}
      return self.render_to_response({'food_formset':formset})
    
    def post(self, *args, **kwargs):
      formset = forms.FoodFormSet(data=self.request.POST, auto_id=False)
      if formset.is_valid():
        formset.save()
        user = self.request.user.id
        return redirect(reverse_lazy('food:home',  kwargs={'username': user}))
 

class DailyFoodList(ListView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  template_name = 'food/testTable.html'
  model = Food
  context_object_name = 'all_food'
  paginate_by = 10

  def get_queryset(self):
    return Food.objects.filter(mealDate = date.today())#.select_related('food')