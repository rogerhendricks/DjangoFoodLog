from django.urls import path
from .views import FoodCreate, FoodList

app_name = 'fooddb'
urlpatterns = [
    path('create/', FoodCreate.as_view(), name='create'),
    path('index/',FoodList.as_view(), name='list'),
]