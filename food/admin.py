from django.contrib import admin
from .models import Food


# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
