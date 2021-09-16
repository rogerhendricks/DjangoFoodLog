from django.urls import path
from .views import SignupPageView, UserPageView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path("",UserPageView.as_view(), name="home"),
]
