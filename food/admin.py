from django.contrib import admin
from.models import Food, TestFood

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(TestFood)
class TestFood(admin.ModelAdmin):
  pass