from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.views.generic import (TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class UserPageView(LoginRequiredMixin,TemplateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  template_name = 'users/index.html'
