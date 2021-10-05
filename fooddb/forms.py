from django import forms
from django.forms import formset_factory
from .models import (Food)

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = [
            "name",
            "fats",
            "sat_fats",
            "carbohydrate",
            "sugars",
            "protein",
            "salt",
            "calories",
            "fat_ratio",
            "carb_ratio",
            "protein_ratio",
            "serving_size"
        ]
        labels = {
          'name':'Name',
          'fat': 'Fat',
          'sat_fats':'Saturated Fats',
          'carbohydrate': 'Carbohydrate',
          'sugars':'Sugars',
          'protein': 'Protein',
          'salt':'Salt',
          'calories': 'Calories',
          'fat_ratio': 'Fat Ratio',
          'carb_ratio': 'Carb Ratio',
          'protein_ratio': 'Protein Ratio',
          'serving_size':'Serving Size'
        }