
from django.urls import path
from .views import MealPageView, FoodCreate, FoodList, FoodUpdate, FavoriteList, DailyFoodList, FoodAdd

app_name = 'food'
urlpatterns = [
    path('index/',MealPageView.as_view(), name="home"),
    path('create/', FoodCreate.as_view(), name='create'),
    path('daily/', FoodList.as_view(), name='daily'),
    path('<int:pk>/update/', FoodUpdate.as_view(), name='update'),
    path('addFavorite/', FavoriteList.as_view(), name='favorites'),
    path('dailyfood/', DailyFoodList.as_view(), name='dailyfood'),
    path('addfood/', FoodAdd.as_view(), name='addfood'),
]