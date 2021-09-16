from django import forms
from django.forms import formset_factory
from .models import (Food, DailyFood)

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = [
            "mealDate",
            "meal",
            "name",
            "serving",
            "fats",
            "carbohydrate",
            "protein",
            "calories",
            "fat_ratio",
            "carb_ratio",
            "protein_ratio",
            "favorite",
            #"client"
        ]
        labels = {
          'mealDate': 'Meal Date',
          'meal': 'Meal',
          'name':'Name',
          'serving':'Serving',
          'fat': 'Fat',
          'carbohydrate': 'Carbohydrate',
          'protein': 'Protein',
          'calories': 'Calories',
          'fat_ratio': 'Fat Ratio',
          'carb_ratio': 'Carb Ratio',
          'protein_ratio': 'Protein Ratio',
          'favorite':'Favorite',
        }
        widgets = {
            #"client": forms.HiddenInput(),
            "mealDate": forms.DateInput(attrs={"class": "datepicker", "type": "date"}),
        }

#favoriteFormset = formset_factory(FoodForm, absolute_max=10)

class DailyFoodForm(forms.ModelForm):


  class Meta:
    model = DailyFood
    fields = [
      "client",
      "Day",
      "daily_calories",
      "daily_fat_ratio",
      "daily_carb_ratio",
      "daily_protein_ratio",
    ]
    labels = {
      'Day': 'Day',
      'daily_calories0': 'Total Calories',
      'daily_fat_ratio': 'Fat Ratio',
      'daily_carb_ratio': 'Carbohydrate Ratio',
      'daily_protein_ration': 'Protein Ration'
    }
    widgets = {
      "client": forms.HiddenInput(),
      "Day": forms.DateInput(attrs={"class": "datepicker", "type": "date"}),
    }
