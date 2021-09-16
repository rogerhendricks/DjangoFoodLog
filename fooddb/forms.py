from django import forms
from django.forms import formset_factory
from .models import (Food, DailyFood)

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = [
            
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
          'name':'Name',
          'fat': 'Fat',
          'carbohydrate': 'Carbohydrate',
          'protein': 'Protein',
          'calories': 'Calories',
          'fat_ratio': 'Fat Ratio',
          'carb_ratio': 'Carb Ratio',
          'protein_ratio': 'Protein Ratio',
        }