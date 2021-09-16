from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,DetailView,
                                    CreateView, DeleteView, UpdateView, 
                                    FormView, View)
# Login and Permissions
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Error Pages
def permission_denied_view(request, exception):
    return render(request, 'errors/403.html')

# Base pages.
class HomePageView(LoginRequiredMixin,TemplateView):
  login_url = '/accounts/login/'
  redirect_field_name = 'redirect_to'
  template_name = 'exercise/index.html'
